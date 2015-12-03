#coding:utf-8
import sys

argvs = sys.argv

i=0

for line in open(argvs[1],'r'):
    i+=1

print i
