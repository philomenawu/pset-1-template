#purpose: output: object's label, accession no., date, place, agents, departments, classifications, references (i.e. printing program)

import argparse
parser = argparse.ArgumentParser(prog='lux.py', allow_abbrev=False)

parser.add_argument('id', help='the id of the object whose details should be shown')

args=parser.parse_args()