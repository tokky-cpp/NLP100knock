#coding:utf-8
import sys

file=sys.argv[1]

lines=[]

for line in open(file,'r'):
    lines.append(line.split('\t'))  

lines.sort(key=lambda x:x[2])

for line in lines:
    str = '\t'.join(line).rstrip()
    print str



