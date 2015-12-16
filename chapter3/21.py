
#coding:utf-8

import json

english = open('english.txt','r')

for line in english:
    if 'Category' in line:
        print line.rstrip()
