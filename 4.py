str_src="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

one=[1, 5, 6, 7, 8, 9, 15, 16, 19]

str=str_src.split(' ')

dic={}

for i in range(len(str)):
    if(i+1 in one):
        print str[i][0]
        dic.setdefault(str[i][0],i+1)
    else:
        print str[i][0:2]
        dic.setdefault(str[i][0:2],i+1)



print dic
#print str
