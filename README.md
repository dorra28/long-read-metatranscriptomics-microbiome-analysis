# long-read-metatranscriptomics-microbiome-analysis
Pipeline for long-read metatranscriptomics analysis of BSFL gut microbiome.
# Long-Read Metatranscriptomics Analysis of BSFL Gut Microbiome

This repository contains a complete pipeline for analyzing long-read metatranscriptomic data from a microbiome dataset using SqueezeMeta. The dataset focuses on the gut microbiome of black soldier fly larvae (BSFL) reared on lignocellulose-rich diets, revealing key lignocellulolytic enzymes.

## Dataset Details
- **Source**: NCBI SRA BioProject [PRJNA866094]([https://www.ncbi.nlm.nih.gov/bioproject/PRJNA866094](https://www.ncbi.nlm.nih.gov/bioproject/?term=PRJNA866094).
- **Description**: Metatranscriptomics of BSFL gut samples from different diets (e.g., brewers' spent grain, wheat bran). 5 samples, Oxford Nanopore MinION sequencing (single-end long reads).
- **Accessions**: SRX17018966, SRX17018967, SRX17018968, SRX17018969, SRX17018970.
- **Study Reference**: Tegtmeier et al. (2023). *Frontiers in Microbiology*. [Link](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2023.1120224/full).

## Tools and Requirements
- **SqueezeMeta**: Automated pipeline for metatranscriptomics. Supports ONT long reads.
- **Installation**: Via Conda (see below).
- **System Requirements**: Linux, 64GB+ RAM, 1TB+ storage.
- **Databases**: SqueezeMeta requires ~700GB for databases (NCBI, eggNOG, etc.). Download once.

## Setup and Installation
1. Install Conda if not already[](https://docs.conda.io/en/latest/miniconda.html).
2. Create and activate SqueezeMeta environment:
conda install -n base conda-libmamba-solver
conda config --set solver libmamba
conda create -n squeezemeta -c conda-forge -c bioconda -c fpusan squeezemeta=1.7 --no-channel-priority --override-channels
conda activate squeezemeta
3. Download SqueezeMeta databases (run in a directory with enough space, e.g., `/opt/databases`):
   Set environment variable: `export SQM_DB_DIR=/path/to/databases`.

4. Install SRA Toolkit for data download: `conda install -c bioconda sra-tools`.

## Usage
1. Download data: `./download_data.sh`
- This creates a `raw_data/` directory with FASTQ files.

2. Prepare samples file: Use the provided `samples.txt` (tab-delimited: sample_name, read_file).

3. Run the pipeline: `./run_pipeline.sh`
- Mode: Co-assembly (combines all samples for better assembly).
- Output: In `output/` directory (taxonomic profiles, functional tables, contigs, etc.).

## Pipeline Steps (Handled by SqueezeMeta)
- **Quality Control**: Trimming and filtering.
- **Assembly**: Flye for long reads (`-a flye`).
- **Mapping**: Minimap2 for ONT (`-map minimap2-ont`).
- **Annotation**: Gene prediction (Prodigal), functional (Diamond vs. databases), taxonomic (LCA).
- **Binning and Abundance**: MAG recovery, transcript abundance estimation.
- **Outputs**: Tables (e.g., `project.abundances.txt`), FASTA files, stats.

## Results Interpretation
- Taxonomic profiles: In `output/project.taxa.txt`.
- Functional profiles: KEGG/COG in `output/project.functions.txt`.
- For visualization: Use R or Python (e.g., load tables into pandas for plots).

## Citation
- SqueezeMeta: Puente-Sánchez et al. (2020). *Microbial Biotechnology*.
- Dataset: Tegtmeier et al. (2023).
- If you use this repo, credit the original tools and data.

## License
MIT License.

File 2: download_data.sh
Bash#!/bin/bash

# Create directory for raw data
mkdir -p raw_data

# List of SRA accessions
ACCESSIONS="SRX17018966 SRX17018967 SRX17018968 SRX17018969 SRX17018970"

# Download each using fastq-dump (single-end, so no split)
for ACC in $ACCESSIONS; do
    fastq-dump --outdir raw_data --gzip $ACC
    mv raw_data/${ACC}.fastq.gz raw_data/${ACC}_1.fastq.gz  # Rename for SqueezeMeta (expects _1 for single-end)
done

echo "Data downloaded to raw_data/"
