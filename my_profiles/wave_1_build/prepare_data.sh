#!/bin/bash
python extract_seqs.py --nextmeta ../../data/metadata_2021-03-12_18-27.tsv --nextfasta ../../data/sequences_2021-03-12_09-14.fasta --query "~((division=='Ontario') & (date>='2020-07-01'))" --include_reference --exclude_incomplete_dates --output ../../data/wave1/wave1

