#coding: utf-8

#input is (word or char list, 'n'-gram)
#引数は、(単語もしくは、単一文字のリスト,n-gramのn)
def gram(list,n):
    n_gram=[]
    for i in range(len(list)-n+1):
        n_gram.append(list[i:i+n])
    return n_gram

#sample data
#サンプルデータ
sentence="I am an NLPer"
list_char=[c for c in sentence]
list_word=sentence.split(' ')

#sample execute
#サンプル実行
n=2
print 'char',n,'gram',gram(list_char,n)
print 'word',n,'gram',gram(list_word,n)
