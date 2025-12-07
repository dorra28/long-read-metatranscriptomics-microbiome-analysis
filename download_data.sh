#!/bin/bash

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
