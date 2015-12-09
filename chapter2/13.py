#coding:utf-8

for one,two in zip(open('col1.txt','r'),open('col2.txt','r')):
    print one.rstrip()+'\t'+two.rstrip()

