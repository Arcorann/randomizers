#!/usr/bin/python2
import re, sys
from multiprocessing import Pool, cpu_count

import load
from analysis import analyze
import compare

count = 100000
if '--fast' in sys.argv:
    count = 10000

# end config

def process(t):
    name, factory = t
    r = factory()
    s = ''
    for i in range(count):
        s += r.next()
    a = analyze(s)
    print '...', name
    return (name, a)

pool = Pool(cpu_count())
m = pool.map(process, sorted(load.rands.items()))
print
for t in m:
    name, a = t
    print name
    for k, v in sorted(a.items()):
        if not re.search(r'_[jiltsoz]$', k):
            print '    %s: %s' % (k, v)
            compare.addelement(name, k, v)
    print

compare.similarity()
