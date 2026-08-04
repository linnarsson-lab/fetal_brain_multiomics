# fetal_brain_multiomics
[Mannens, C.C.A., Hu, L., Lönnerberg, P. et al. Chromatin accessibility during human first-trimester neurodevelopment. Nature (2024). https://doi.org/10.1038/s41586-024-07234-1](https://www.nature.com/articles/s41586-024-07234-1)

## The loom files and cell ranger outputs hosted on this page are temporarily unavailable. Please access the data either through the EGA or download processed data from CELLxGENE or CATlas. 

## Download the loom files
  
[Pool_peaks.loom](https://www.dropbox.com/scl/fi/hozow8gaub1rjckgp93lp/Pool_peaks.loom.gz?rlkey=ssp97d68ktyv8ohpsf0mwxlz9&st=ub33iuq1&dl=1)

[Pool_peaks.agg.loom](https://www.dropbox.com/scl/fi/zotdkbjwcr7gjoif7ow3l/Pool_peaks.agg.loom.gz?rlkey=gu9ropm9qx5dqy1llsxvds5dl&st=o4077q29&dl=1)

[Pool_RNA.loom](https://www.dropbox.com/scl/fi/vu2m6tfxzpahopk85q0bx/Pool_RNA.loom.gz?rlkey=kui3mr83ukojzjg4zsmobsh10&st=5kxv3oua&dl=1)

[Pool_RNA.agg.loom](https://www.dropbox.com/scl/fi/p3phh8n4nhtm4ou8x2r90/Pool_RNA.agg.loom?rlkey=uz6nkgok6blar49owvi7y8kxr&st=9i4j2rod&dl=1)

[Pool_GA.loom](https://www.dropbox.com/scl/fi/9ollr4avd508tc6dhx2hv/Pool_GA.loom?rlkey=h2gw3lj9ti7wne0uo29ztjwk0&st=owwrlrsp&dl=1)

[Pool_GA.agg.loom](https://www.dropbox.com/scl/fi/ghl28tz0hqjcivzw3pp6j/Pool_GA.agg.loom?rlkey=i7eofvjjfzlhhc61yxuh3av0f&st=8in77okq&dl=1)

[Pool_motifs.agg.loom](https://www.dropbox.com/scl/fi/44jjsjcfybnum9xn3b63m/Pool_motifs.agg.loom?rlkey=z6jxocrm2iyjul769f8yrspxo&st=ygy2vo1q&dl=1)

[Pool_subset_RNA.loom](https://www.dropbox.com/scl/fi/vu2m6tfxzpahopk85q0bx/Pool_RNA.loom.gz?rlkey=kui3mr83ukojzjg4zsmobsh10&st=5kxv3oua&dl=1)

[Purkinje_RNA.loom](https://www.dropbox.com/scl/fi/9w3o2ddq6yg19zr5tfka2/Purkinje_RNA.loom.gz?rlkey=t22f4lttc2wocalb8b700knf4&st=eg1vaz5a&dl=1)

[Purkinje_RNA.agg.loom](https://www.dropbox.com/scl/fi/xxyu3ow907b77raszzc1u/Purkinje_RNA.agg.loom?rlkey=hmsref739z3dd53zvrt97fw77&st=s803ih66&dl=1)

[Purkinje_chromVAR.loom](https://www.dropbox.com/scl/fi/j6bilrrbdv907gq5s0ygz/Purkinje_chromVAR.loom?rlkey=bpnbrmxipcqjjaqfhebs7zdxb&st=m70va4j9&dl=1)

[Purkinje_peaks.loom](https://www.dropbox.com/scl/fi/bpqxlgzxsdj4h0f8d2k3y/Purkinje_peaks.loom.gz?rlkey=m0trhqzf3fe8iw5tr5ucrl35i&st=c0ohruf8&dl=1)

[Purkinje_peaks.agg.loom](https://www.dropbox.com/scl/fi/c7gm7slkc8rxlrqgn0oje/Purkinje_peaks.agg.loom?rlkey=xsn9tan47a7qwego2060ygtj3&st=sfbogjjl&dl=1)

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

## Other access points to the processed data
- [CELLxGENE](https://cellxgene.cziscience.com/collections/a66d41a7-f1de-4b70-b983-7a4b790a0d5d): multiome data is available in anndata format or as fragment files.
- [CATlas](https://catlas.org/humanbraindev/#!/): here you can download bigwig files, candidate cCREs and predicted gene-cCRE links.
- 
## Cellranger-arc outputs

Available [here](https://www.dropbox.com/scl/fo/1ummj0m1ya2bu645mv9nl/AP_KCviN53gEa-SoiFCDVnE?rlkey=ypol98tifeho01541n8rz3mm3&st=an8e4h4i&dl=0).

## Raw sequence data

Raw sequencing data are available through from the European Genome Phenome Archive [EGAS00001007472](https://ega-archive.org/studies/EGAS00001007472).

Our gene and transcript annotations used for the [cellranger-arc](https://www.10xgenomics.com/support/software/cell-ranger-arc/latest) pipeline are based on Based on GRCh38.p13 gencode V35 primary sequence assembly as previously described in [Emelie Braun et al., Science 2023](https://www.science.org/doi/10.1126/science.adf1226). 

We discarded genes or transcripts that overlapped or mapped to other genes or non-coding RNAs 3’ UTR.

From [this link](https://www.dropbox.com/scl/fi/n0lzymiyt4u42pzj4vzvj/refdata-cellranger-arc-hg38-final3.tgz?rlkey=3qrgtlpnrwge8zbx7wb9pwxia&st=bl7vnv4c&dl=1) you can download the input files to build the cellranger-arc index yourself.

For more information please see [the corresponding github repo](https://github.com/linnarsson-lab/developing-human-brain).

A list of all sample names can be found in [10X_output](https://github.com/linnarsson-lab/fetal_brain_multiomics/blob/main/files/10X_output_samples.txt), and the metadata providing region, name, sample ID etc can be found in [Extended data 1](https://github.com/linnarsson-lab/fetal_brain_multiomics/blob/main/files/supplementals/Extended_data_1_sample_data.xlsx)

## Preprint (bioRxiv)

[biorxiv](https://www.biorxiv.org/content/10.1101/2023.08.18.553878v1)

## Code
We use the [Chromograph](https://github.com/linnarsson-lab/chromograph) pipeline.

Code for making many of the figures is available as [Jupyter notebooks](notebooks/README.md)
The package versions used to generate these figures are in [this environment file](environment.yml)

