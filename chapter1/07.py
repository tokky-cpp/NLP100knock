#coding:utf-8

def make_sentence(a,b,c):
    sentence = u'%s時の%sは%s' %(a,b,c)
    return sentence

#サンプル入力
a = 12
b = u'気温'
c = 22.4

print make_sentence(a,b,c)
