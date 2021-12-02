#!/usr/bin/env python3

import os,gzip
from Bio import SeqIO
from Bio.Seq import Seq

URL='https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/015/565/GCF_000015565.1_ASM1556v1/GCF_000015565.1_ASM1556v1_protein.faa.gz'
fasta=os.path.basename(URL)
if not os.path.exists(fasta):
    os.system("curl -O {}".format(URL))

#TODO
# Figure out how you will keep track of the output filename
# take a set of sequences and write out when you get to a certain number
# determine a new filename for the output

seqs_to_write = []
with gzip.open(fasta,"rt") as infh:
    for seq_record in SeqIO.parse( infh , "fasta"):
        print(seq_record.id)
