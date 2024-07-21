#!/usr/bin/env python

# You can refer to the help manual by `python parse_gtf.py -h`

import argparse
import csv
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help='The input file specified will be the GTF file provided by snakemake',dest="input", required=True)
parser.add_argument("-o", "--output", help='The output file name and path provided by snakemake',dest="output", required=True)

args = parser.parse_args()

import csv

ids = []
names = []

with open(args.input, 'rt') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        if row[0][0] == '#':
            continue
        else:
            if row[2] == 'gene':
                gene_info = row[8].strip().split('; ')
                splits = [_.split('"') for _ in gene_info]
                for l in splits:
                    if l[0].strip() == 'gene_id':
                        ids.append(l[1])
                    if l[0].strip() == 'gene_name':
                        names.append(l[1])

with open(args.output, 'wt') as w:
    for geneid, genename in zip(ids, names):
        w.write('{}\t{}\n'.format(geneid, genename))
