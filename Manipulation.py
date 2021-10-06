import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer

#Preparing the txt file
textfile = open("D:\\EasyAccess\\txt_911.txt", mode = "r")
raw = textfile.read()

#creating the tokens
tokens = nltk.word_tokenize(raw)

#Making the stop word list
sWords = set(stopwords.words("english"))
sWords_list = list(sWords)
punc = [".", ",", "?", ";", ":", "'", '"', "\\", "-", "&", "$", "#", "[", "]", "{", "}", "|", "/", "_"]
for i in punc:
    if i not in sWords_list:
        sWords_list.append(i)

#Creating a new list without the stop words
filteredlist = []
for j in tokens:
    if j not in sWords_list:
        filteredlist.append(j)

#Part of Speech Tagging
pos = nltk.pos_tag(filteredlist)
print(pos)

#Lemmitization
lem = WordNetLemmatizer()
#for term in filteredlist:
#    print(lem.lemmatize(term, "n"))