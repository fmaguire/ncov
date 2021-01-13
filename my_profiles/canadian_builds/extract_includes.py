#!/usr/bin/env python

import pandas as pd

df = pd.read_csv('../../data/2021_01_11/metadata_2021-01-08_18-19.tsv', sep='\t')

# filter to canada
df = df[df['country'] == 'Canada']

df = df[df['pangolin_lineage'].isin(['B.1.1.7', 'B.1.351', 'B.1.36.17', 'B.1.1.248'])]

print()
for strain in df['strain'].values:
    print(strain)


