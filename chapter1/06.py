#coding: utf-8

str1="paraparaparadise"
str2="paragraph"

str_char1=[c for c in str1]
str_char2=[c for c in str2]


#input is (word or char list, 'n'-gram)
#引数は、(単語もしくは、単一文字のリスト,n-gramのn)
def n_gram(list,n):
    n_gram_list=[]
    for i in range(len(list)-n+1):
        n_gram_list.append(''.join(list[i:i+n]))
    return n_gram_list


x_bi=n_gram(str_char1,2)
y_bi=n_gram(str_char2,2)

x=set(x_bi)
y=set(y_bi)

print "和集合(x∪y)",x.union(y)
print "積集合(x∩y)",x.intersection(y)
print "差集合(x-y)",x.difference(y)
print "差集合(y-x)",y.difference(x)

if 'se' in x:
    print "\'se\' is in X"
else:
    print "\'se\' is not in X"

if 'se' in y:
    print "\'se\' is in Y"
else:
    print "\'se\' is not in Y"


