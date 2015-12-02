#coding:utf-8

def cipher(sentence):
    cip=''
    for c in sentence:
        if 'a'<=c and c<='z':
            cip += chr(219-ord(c))
        else:
            cip += c
    return cip

plain = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'

print 'plain text'
print plain

secret = cipher(plain)
print '\nsecret text'
print secret

decrypt = cipher(secret)
print '\ndecrypted text'
print decrypt
