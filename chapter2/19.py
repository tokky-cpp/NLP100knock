#coding:utf-8
import sys

file=sys.argv[1]

lines=[]

for line in open(file,'r'):
    lines.append(line.split('\t'))  

pcount = {}

for line in lines:
    pcount.setdefault(line[0],0)
    pcount[line[0]]+=1

pcount_sorted = sorted(pcount.items(),key=lambda x:x[1])

pcount_sorted.reverse()

for i in pcount_sorted:
    for j in i:
        print j,
    print 
