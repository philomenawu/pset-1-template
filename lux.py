#purpose: display table of objects filtered by: department, agent, classification, title (i.e. sorting program)

import argparse
parser = argparse.ArgumentParser(prog='lux.py', allow_abbrev=False)

parser.add_argument('-d', metavar='--date', help='show only those objects whose date contains date')
parser.add_argument('-a', metavar='--agt', help='show only those objects produced by an agent with name containing agt')
parser.add_argument('-c', metavar='--cls', help='show only those objects classified with a classifier having a name containing cls')
parser.add_argument('-l', metavar='--label', help='show only those objects whose label contains label')

args=parser.parse_args()


