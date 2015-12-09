#coding:utf-8

import sys

n = int(sys.argv[1])
file = sys.argv[2]

lines = list(open(file,'r'))

if n > len(lines):
    n = len(lines)

for line in lines[-n:]:
    print line.rstrip()

