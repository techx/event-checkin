#!/usr/bin/env python

import subprocess, re, json

INFILE = 'athenas.txt'
OUTFILE = '../studentinfo.json'
SEARCHES = {
    'name': r'^cn: (.*)$',
    'year': r'^mitDirStudentYear: (.)$',
    'course': r'^ou: (.*)$'
}

COMPILED_SEARCHES = {
    query: re.compile(pattern, re.MULTILINE)
        for query, pattern in SEARCHES.items()
}

def main():
    with open(INFILE) as fin:
        users = [i.strip() for i in fin.read().split()]
        info = { user: process_user(user)
            for user in users }
        with open(OUTFILE, 'w') as fout:
            jstr = json.dumps(info, sort_keys = True, indent = 4,
                separators = (',', ': '))
            fout.write('%s\n' % jstr)

def process_user(user):
    print 'Processing user %s' % user
    cmd = ['ldaps', user, 'mitDirStudentYear', 'cn', 'ou']
    proc = subprocess.Popen(cmd,
        stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    res = proc.stdout.read()
    def search(pattern):
        match = pattern.search(res)
        if match:
            return match.group(1)
        else:
            return None
    return {
        query: search(pattern)
            for query, pattern in COMPILED_SEARCHES.items()
            if search(pattern) is not None
    }

if __name__ == '__main__':
    main()
