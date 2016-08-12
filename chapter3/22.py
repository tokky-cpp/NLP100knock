
#coding:utf-8

import json
import re

english = open('english.txt','r')

pattern = re.compile(u"\[\[Category:(.*)\]\]")

for line in english:
    matchs = re.finditer(pattern,line)
    for match in matchs:
        print match.groups()[0]

#example:
#[[Category:君主国]]

#参考
# http://symfoware.blog68.fc2.com/blog-entry-1800.html
