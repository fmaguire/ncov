#!/usr/bin/env python

import pandas as pd
import sys

df = pd.read_csv(sys.argv[1], sep='\t')

# filter to canada
df = df[df['country'] == 'Canada']

df = df[df['pangolin_lineage'].isin(['B.1.1.7', 'B.1.351', 'P.1', "P.2"])]

print()
for strain in df['strain'].values:
    print(strain)


