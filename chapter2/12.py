#coding:utf-8
import sys

argvs=sys.argv

lines=[]

one = open("col1.txt",'w')
two = open("col2.txt",'w')

for line in open(argvs[1],'r'):
    lines.append(line.split('\t'))  

for line in lines:
    one.write(line[0]+'\n')
    two.write(line[1]+'\n')
