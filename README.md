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

The `.agg` files are aggregate files where each column represents a cluster in the main loom-file with the same name.

## Description of values in the cell-metadata of loom files:

- Age: Age as reported by the clinician in post-conceptional weeks
- barcode: 10X barcode
- CellCyle: Fraction of RNA reads in Cell cylcle genes.
- CellID: Unique cell identifier in the form of sample:barcode
- Chemistry: The 10X genomics kit used to acquire the cell
- Class: Broad annotation of cell classes (Radial glia, Neuron, Oligo etc)
- ClusterName: Annotated cluster name
- Clusters: Cluster IDs used in the paper, result of subclustering and merging of class subsets
- Clusters_main: Primary clusters derived from analysis prior to subsetting of data
- Donor: Donor IDs (same as Shortname)
- DoubletFinderScore/Flag: Output from Doubletfinder
- Embedding: 2D embedding as used in the paper (TSNE/UMAP both available as well)
- FRIP: Fraction of Reads in Peak (ATAC)
- FRtss: Fraction of Reads in tss
- GA_colsum: summed gene accessibility per cell
- Id: ID from database
- LSI: Latent Semantic Indexing (LSI_b is LSI over bins, LSI_main is LSI after pooling of subsets)
- Method: Either 'atac-seq' or 'rnaXatac'
- mitochondrial: Number of mitochondrial reads (ATAC)
- Name: Library ID
- NBins/NGenes/NPeaks: Number of positive bins/genes/peaks
- passed_filters: Number of fragments (ATAC)
- peak_region_fragments/cutsites: As reported by cellranger-arc
- preClusters: Basic clustering based on binned data used for peak calling
- PseudoAge: Age smoothed over nearest neighbors
- SEX: Sex as determined based on Y-chromosomal reads
- TSNE/UMAP: Embedding as computed prior and post (_main) pooling of subsets
- TSS_fragments: Total number of TSS fragments (ATAC)
- Tissue/regions/subregions: Region annotation
- total: total reads (ATA)
- TotalUMI: Total number of UMIs (RNA)
- Y: Fraction of Y-chromosomal reads

## Layers in RNA files:
- Z: Z-score normalization
- Ambiguous: ambiguously mapped reads as returned by velocyto
- Norm: Depth-normalized counts
- Pooled: Here each value is pooled from the 10 nearest multiome neighbours (depth normalized), i.e. also ATAC-only cells will have an imputed value here. Base layer is identical to pooled layer
- Raw: only the measured counts (multiome)
- Spliced: only the spliced counts (velocyto)
- Spliced_pooled: similar to pooled, but only spliced counts
- Unspliced/unspliced_pooled: unspliced counts (Velocyto)

## Layers in Peak files:
- '': Base layer contains binarized counts
- 'Counts': Counts per peak

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
