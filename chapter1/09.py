#coding:utf-8
import random

def substitution(word):
    if len(word)<=4:
        return word
    else:
        change = word[0]
        char = [c for c in word[1:-1]]
        for i in range(len(char)):
            change += char.pop(random.randint(0,len(char)-1))
        change += word[-1]
        return change

#sample sentence
sentence = 'I couldn\'t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'

#sentence to word_list
secret = sentence.split()

#encryption
secret = [substitution(word) for word in secret]

#word_list to sentence
print ' '.join(secret)
