
#coding:utf-8

import json
import re

english = open('english.txt','r')

target = re.compile(u"Category")

for line in english:
    if target.search(line):
        print line
