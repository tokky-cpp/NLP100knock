#coding:utf-8

import json


file = open("jawiki-country.json","r")
output = open("english.txt","w")

for line in file:
    data = json.loads(line)

    if u'イギリス' in data[u'text']:
        output.write(data[u'text'].encode('utf8'))
        print data[u'title']
