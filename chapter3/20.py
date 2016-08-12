#coding:utf-8

import json

file = open("jawiki-country.json","r")
output = open("english.txt","w")

for line in file:
    data = json.loads(line)

    if u'イギリス' in data[u'text']:
        output.write(data[u'text'].encode('utf8'))
        print data[u'title']

file.close()
output.close()


#__author__ = 'todoroki'

#import re
#import json

#inputfile = 'jawiki-country.json'
#outputfile = 'jawiki-england.txt'

#f = open(inputfile)
#g = open(outputfile, 'w')

#target = re.compile(u'イギリス')

#for line in f:
#    res = json.loads(line)
#    if target.search(res[u'text']):
#        g.write(res['text'].encode('utf8') + '\n')
#f.close()
#g.close()
