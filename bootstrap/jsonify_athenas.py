#!/usr/bin/env python

import subprocess, os, itertools, json

INFILE = 'athenas.txt'
OUTFILE = '../athenas.json'

DIR = os.path.dirname(os.path.realpath(__file__))
ABS_INFILE = os.path.join(DIR, INFILE)
ABS_OUTFILE = os.path.join(DIR, OUTFILE)

def main():
    with open(ABS_INFILE) as fin:
        users = [i.strip() for i in fin.read().split()]
        info = { ltr: sorted(list(names))
            for ltr, names in itertools.groupby(users, lambda s: s[0])  }
        with open(ABS_OUTFILE, 'w') as fout:
            jstr = json.dumps(info, sort_keys = True, indent = 4,
                separators = (',', ': '))
            fout.write('%s\n' % jstr)

if __name__ == '__main__':
    main()
