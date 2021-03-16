mkdir -p ../../data/wave_1; python extract_seqs.py --exclude_incomplete_dates --query "date < '2020-07-01'" --nextmeta metadata_2021-01-22_08-51.tsv.gz --nextfasta sequences_2021-01-22_08-52.fasta.gz --out
put_prefix ../../data/wave_1/wave_1_data


