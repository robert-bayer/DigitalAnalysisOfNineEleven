import nltk
from nltk import word_tokenize

mystring = "The dog ran over the cat on its way to the food."

tokens = nltk.word_tokenize(mystring)

print(tokens)

pos = nltk.pos_tag(tokens)

print(pos)

for tags in pos:
    for char in tags:
        print(char)