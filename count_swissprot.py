#!/usr/bin/env python3

import re
import os
import gzip
URL='https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.fasta.gz'
fasta=os.path.basename(URL)
if not os.path.exists(fasta):
    os.system("curl -O {}".format(URL))

with gzip.open(fasta,"rt") as infh:
    for line in infh:
        if line.startswith('>'):
            print(line)
