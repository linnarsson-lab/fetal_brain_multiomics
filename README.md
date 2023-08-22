# fetal_brain_multiomics
*Dynamics of chromatin accessibility during human first-trimester neurodevelopment* (Camiel Mannens et al. 2023, in review).

![fig1.pdf](https://github.com/linnarsson-lab/fetal_brain_multiomics/files/12143211/fig1.pdf)

## Download the loom files

[Pool_peaks.loom](https://storage.googleapis.com/linnarsson-lab-human/ATAC_dev/Pool_peaks.loom)

[Pool_peaks.agg.loom](https://storage.googleapis.com/linnarsson-lab-human/ATAC_dev/Pool_peaks.agg.loom)

[Pool_RNA.loom](https://storage.googleapis.com/linnarsson-lab-human/ATAC_dev/Pool_RNA.loom)

[Pool_RNA.agg.loom](https://storage.googleapis.com/linnarsson-lab-human/ATAC_dev/Pool_RNA.agg.loom)

[Pool_GA.loom](https://storage.googleapis.com/linnarsson-lab-human/ATAC_dev/Pool_GA.loom)

[Pool_GA.agg.loom](https://storage.googleapis.com/linnarsson-lab-human/ATAC_dev/Pool_GA.agg.loom)

[Pool_motifs.agg.loom](https://storage.googleapis.com/linnarsson-lab-human/ATAC_dev/Pool_motifs.agg.loom)

[Pool_subset_RNA.loom](https://storage.googleapis.com/linnarsson-lab-human/ATAC_dev/Pool_subset_RNA.loom)

[Purkinje_RNA.loom](https://storage.googleapis.com/linnarsson-lab-human/ATAC_dev/Purkinje_RNA.loom)

[Purkinje_RNA.agg.loom](https://storage.googleapis.com/linnarsson-lab-human/ATAC_dev/Purkinje_RNA.agg.loom)

[Purkinje_chromVAR.loom](https://storage.googleapis.com/linnarsson-lab-human/ATAC_dev/Purkinje_chromVAR.loom)

[Purkinje_peaks.loom](https://storage.googleapis.com/linnarsson-lab-human/ATAC_dev/Purkinje_peaks.loom)

[Purkinje_peaks.agg.loom](https://storage.googleapis.com/linnarsson-lab-human/ATAC_dev/Purkinje_peaks.agg.loom)

## Preprint (bioRxiv)

[biorxiv](https://www.biorxiv.org/content/10.1101/2023.08.18.553878v1)

## Code
We use the [Chromograph](https://github.com/linnarsson-lab/chromograph) pipeline.

Code for making many of the figures is available as [Jupyter notebooks](notebooks/README.md)

### Genes and transcripts annotation

Our gene and transcripts annotation is based on Based on GRCh38.p13 gencode V35 primary sequence assembly as previously described in [Emelie Braun et al., 2022, in review](https://www.biorxiv.org/content/10.1101/2022.10.24.513487v1). 

We discarded genes or transcripts that overlapped or mapped to other genes or non-coding RNAs 3’ UTR.

The GTF file used for read counts: [gb_pri_annot_filtered.gtf](https://storage.googleapis.com/linnarsson-lab-tmp/gb_pri_annot.gtf)

The genes and transcripts that were discarded: [filtered_transcripts.txt](https://storage.googleapis.com/linnarsson-lab-tmp/filtered_transcripts.txt)
