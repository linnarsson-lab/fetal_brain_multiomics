## Imports
import numpy as np

from chromograph.pipeline import config
from chromograph.preprocessing.utils import *
from cytograph.visualization.scatter import *
from cytograph.visualization.colors import Colorizer

import torch
from torch import nn
from twobitreader import TwoBitFile
from deeplift.dinuc_shuffle import dinuc_shuffle

from tqdm import tqdm, trange

def one_hot_encoder(enhancers, enhancer_length, f_bit):
    hg38 = TwoBitFile(f_bit)
    enhancer_onehot = np.zeros((len(enhancers), 4, enhancer_length), dtype="float32")
    for ix, enhancer in tqdm(enumerate(enhancers)):
        ch, interval = enhancer.split(":")
        a, b = interval.split("-")
        start = int(a)
        end = int(b)
        seq = hg38[ch][start:end].upper()
        onehot = np.vstack([
            [s == "A" for s in seq],
            [s == "C" for s in seq],
            [s == "G" for s in seq],
            [s == "T" for s in seq]
        ])
        enhancer_onehot[ix, :, :] = onehot
    return enhancer_onehot

## The following funcations have been adapted from TF-MoDisCo, for more details please visit the repository here:
## https://github.com/kundajelab/tfmodisco
def shuffle_several_times(x):
    if (x is None):
        return torch.tensor(np.zeros((100, 4, 249)).astype("float32"))
    else:
        return torch.tensor(np.array([dinuc_shuffle(x.T).T for i in range(100)]).astype("float32"))
    
def combine_mult_and_diffref(mult, orig_inp, bg_data):
    to_return = []
    # Originally for inputs that are in the format (length x 4)
    mult = mult.T
    orig_inp = orig_inp.T
    bg_data = bg_data.T
    for l in range(len(mult)):
        projected_hypothetical_contribs = np.zeros((4,4)).astype("float")
        assert len(orig_inp[l].shape)==2, orig_inp[l].shape
        for i in range(4):
            hypothetical_input = np.zeros(4).astype("float")
            hypothetical_input[i] = 1.0
            hypothetical_difference_from_reference = (hypothetical_input-bg_data[l].T)
            hypothetical_contribs = hypothetical_difference_from_reference*mult[l]
            projected_hypothetical_contribs[:,i] = np.sum(hypothetical_contribs,axis=-1)
        to_return.append(np.mean(projected_hypothetical_contribs,axis=0))
    return np.array(to_return).T

def compute_contrib(cfname, pred_sequences):
    model = deepGBM.ConvolutionalClassificationModel.load_from_checkpoint(cfname, map_location=torch.device('cpu'))
    model.eval()
    explainer = DeepLiftShap(model)

    contrib_scores= []
    norm_scores = []
    for i in trange(len(pred_sequences)):
        onehot_data = pred_sequences[i].numpy()
        explanations = explainer.attribute(torch.tensor(onehot_data[None, :, :]), shuffle_several_times(onehot_data), target=1).detach().numpy()[0]
        dinuc_shuff_explanation = np.sum(explanations, axis=0) * onehot_data
        norm = dinuc_shuff_explanation - np.mean(dinuc_shuff_explanation,axis=0)[np.newaxis,:]
        contrib_scores.append(dinuc_shuff_explanation)
        norm_scores.append(norm)
        
    return contrib_scores, norm_scores