#!/usr/bin/env python

import pandas as pd
import sys

df = pd.read_csv("../../data/wave1_metadata.tsv", sep='\t')

# filter to canada
df = df[df['country'] == 'Canada']

with open('../../defaults/include.txt') as fh:
    default_include = [isolate.strip() for isolate in fh]

with open('include_all_canada_wave_1.txt', 'w') as can_fh:
    for default in default_include:
        can_fh.write(default + "\n")
    for strain in df['strain'].values:
        can_fh.write(strain + "\n")

with open('include_all_ontario_wave_1.txt', 'w') as on_fh:
    on_df = df[df['division'] == 'Ontario']
    for default in default_include:
        on_fh.write(default + "\n")

    for strain in on_df['strain'].values:
        on_fh.write(strain + "\n")

