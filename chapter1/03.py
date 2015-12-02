sentence="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

words=[]
words=sentence.split(' ')
word_len=[]

for w in words:
    if(w[len(w)-1]=='.' or w[len(w)-1]==','):
#           print w[0:len(w)-1],len(w)-1
        word_len.append(len(w)-1)
    else:
#        print w,len(w)
        word_len.append(len(w))

print word_len
