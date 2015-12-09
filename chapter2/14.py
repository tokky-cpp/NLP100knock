#coding:utf-8

import sys

argvs=sys.argv

lines = list(open(argvs[2],'r'))

argvs[1] = int(argvs[1])
if argvs[1]>len(lines):
    argvs[1] = len(lines)

for i in range(int(argvs[1])):
    print lines[i].rstrip()

