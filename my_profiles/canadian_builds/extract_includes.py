#!/usr/bin/env python

import pandas as pd
import sys

df = pd.read_csv(sys.argv[1], sep='\t')

# filter to canada
df = df[df['country'] == 'Canada']

df = df[df['pango_lineage'].isin(['R.1', 'B.1.617.1', 'B.1.617.2', 'B.1.617.3', "B.1.525", 'B.1.526'])]

print()
for strain in df['strain'].values:
    print(strain)


