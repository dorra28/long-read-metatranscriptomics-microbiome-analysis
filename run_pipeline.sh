#!/bin/bash

# Activate environment
conda activate squeezemeta

# Run SqueezeMeta in co-assembly mode for long reads (ONT)
# -p: project name
# -s: samples file
# -f: raw data dir
# -a: assembler (flye for long reads)
# -map: mapper (minimap2-ont for ONT)
# --rna: Flag for metatranscriptomics (enables transcript-focused annotation)
# -t: threads (adjust based on your machine)
SqueezeMeta.pl -m coassembly -p output/project -s samples.txt -f raw_data -a flye -map minimap2-ont --rna -t 16

# Optional: Restart if interrupted
# SqueezeMeta.pl -p output/project --restart

echo "Analysis complete. Results in output/project/"
