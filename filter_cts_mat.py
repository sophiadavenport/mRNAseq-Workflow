#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help='The input file specified will be the concatenated VERSE matrix provided by snakemake',dest="input", required=True)
parser.add_argument("-o", "--output", help='The output file name and path provided by snakemake',dest="output", required=True)

args = parser.parse_args()

import pandas

df = pandas.read_csv(args.input)

sample_cols = [col for col in df.columns if col != 'gene']

filtered = df.loc[(df[sample_cols] != 0).sum(axis=1) == 8]

filtered.to_csv(args.output, index=False)
