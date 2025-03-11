# fetal_brain_multiomics
[Mannens, C.C.A., Hu, L., Lönnerberg, P. et al. Chromatin accessibility during human first-trimester neurodevelopment. Nature (2024). https://doi.org/10.1038/s41586-024-07234-1](https://www.nature.com/articles/s41586-024-07234-1)

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

## Download 10X cellranger output (ATAC/ARC)
To download the 10X output for individual samples use the command below, replacing {sample} with the sample you need. 
A list of all the sample names can be found in [10X_output](https://github.com/linnarsson-lab/fetal_brain_multiomics/blob/main/files/10X_output_samples.txt), and the metadata providing region, name, sample ID etc can be found in [Extended data 1](https://github.com/linnarsson-lab/fetal_brain_multiomics/blob/main/files/supplementals/Extended_data_1_sample_data.xlsx)
```
wget https://storage.googleapis.com/linnarsson-lab-human/ATAC_dev/10X/{sample}
```

## Preprint (bioRxiv)

[biorxiv](https://www.biorxiv.org/content/10.1101/2023.08.18.553878v1)

## Code
We use the [Chromograph](https://github.com/linnarsson-lab/chromograph) pipeline.

Code for making many of the figures is available as [Jupyter notebooks](notebooks/README.md)
The package versions used to generate these figures are in [this environment file](environment.yml)

### Genes and transcripts annotation

Our gene and transcripts annotation is based on Based on GRCh38.p13 gencode V35 primary sequence assembly as previously described in [Emelie Braun et al., 2022, in review](https://www.biorxiv.org/content/10.1101/2022.10.24.513487v1). 

We discarded genes or transcripts that overlapped or mapped to other genes or non-coding RNAs 3’ UTR.

The GTF file used for read counts: [gb_pri_annot_filtered.gtf](https://storage.googleapis.com/linnarsson-lab-tmp/gb_pri_annot.gtf)

The genes and transcripts that were discarded: [filtered_transcripts.txt](https://storage.googleapis.com/linnarsson-lab-tmp/filtered_transcripts.txt)
