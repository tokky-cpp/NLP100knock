#coding:utf-8

dict = {}
for pref in open('col1.txt','r'):
    dict.setdefault(pref,0)

list = dict.keys()

#print list
for w in list:
    print w.rstrip()
