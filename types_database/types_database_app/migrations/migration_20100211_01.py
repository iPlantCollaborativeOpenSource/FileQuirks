# -*- coding: utf-8 -*-
# migration for adding expert data types


import os
import sys
import traceback

BASE_DIR=os.path.split(os.path.split(os.path.split(os.path.split(os.path.abspath(__file__))[0])[0])[0])[0]
#print BASE_DIR
sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'types_database.settings'

from types_database.types_database_app.models import ExpertRegex
from types_database.types_database_app.models import DataType


DEBUG=True

regexes=[
    ["Protein Plain Text Sequence","Protein Plain Text Sequence r1","[ACDEFGHIKLMNPQRSTVWXY]{10,}"],
    ["Plain Nucleotide Sequence","Plain Nucleotide Sequence r1","[auctgAUCTG]{10,}"],
    ["DNA Sequence in FASTA Format","DNA Sequence in FASTA Format r1",">(.*)\n([ACTGNactgn]{10,}(\s*)){1,}"],
    ["RNA Sequence in FASTA Format","RNA Sequence in FASTA Format r1",">(.*)\n([ACUGNacugn]{10,}(\s*)){1,}"],
    ["DNA Sequences in FASTA Format","DNA Sequences in FASTA Format r1","(>([^\t\n\r\f\v]*)\r?\n\r?([ANCTGanctg\n\r]{20,})){2,}"],
    ["RNA Sequences in FASTA Format","FNA Sequences in FASTA Format r1","(>([^\t\n\r\f\v]*)\r?\n\r?([ANCUGauctg\n\r]{20,})){2,}"],
    ["Protein MSA in FASTA Format","Protein MSA in FASTA Format r1","(>([^\t\n\r\f\v]*)\r?\n\r?([-ACDEFGHIKLMNPQRSTVWXY\n\r]{20,})){2,}"],
]


for r in regexes:
    try:
        r=ExpertRegex(
            data_type=DataType.objects.get(name=r[0]),
            name=r[1],
            content=r[2]
        )
        r.save()
    except:
        if DEBUG:
            traceback.print_exc(2)



