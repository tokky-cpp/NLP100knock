# -*- coding: utf-8 -*-
__author__ = 'todoroki'

import re
import json

inputfile = 'jawiki-country.json'
outputfile = 'jawiki-england.txt'

f = open(inputfile)
g = open(outputfile, 'w')

target = re.compile(u'イギリス')

for line in f:
    res = json.loads(line)
    if target.search(res[u'text']):
        g.write(res['text'].encode('utf8') + '\n')
f.close()
g.close()
