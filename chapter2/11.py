#coding:utf-8
import sys

argvs = sys.argv

for line in open(argvs[1],'r'):
    print line.replace('\t',' ').rstrip()
        
