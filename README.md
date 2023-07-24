# fetal_brain_multiomics
Dynamics of chromatin accessibility during human first-trimester neurodevelopment* (Camiel Mannens et al. 2023, in review).

![fig1.pdf](https://github.com/linnarsson-lab/fetal_brain_multiomics/files/12143211/fig1.pdf)

## Preprint (bioRxiv)

Preprint will be online shortly

## Code
We use the [Chromograph](https://github.com/linnarsson-lab/chromograph) pipeline.

Code for making many of the figures is available as [Jupyter notebooks](notebooks/README.md)

### Genes and transcripts annotation

Our gene and transcripts annotation is based on Based on GRCh38.p13 gencode V35 primary sequence assembly as previously described in [Emelie Braun et al., 2022, in review](https://www.biorxiv.org/content/10.1101/2022.10.24.513487v1). 

We discarded genes or transcripts that overlapped or mapped to other genes or non-coding RNAs 3’ UTR.

The GTF file used for read counts: [gb_pri_annot_filtered.gtf](https://storage.googleapis.com/linnarsson-lab-tmp/gb_pri_annot.gtf)

The genes and transcripts that were discarded: [filtered_transcripts.txt](https://storage.googleapis.com/linnarsson-lab-tmp/filtered_transcripts.txt)
