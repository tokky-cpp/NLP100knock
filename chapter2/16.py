#coding:utf-8

import sys

n = int(sys.argv[1])
file = sys.argv[2]

lines = list(open(file,'r'))

files = []

if n > len(lines):
    n = len(lines)

i = 0
for i in range(len(lines)/n):
    files.append(lines[n*i:n*(i+1)])
    i+=1

print files

