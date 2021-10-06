from urllib import request
from bs4 import BeautifulSoup
import nltk
from nltk import word_tokenize
import PyPDF2

url = "https://www.swotandpestle.com/berkshire-hathaway/"
response = request.urlopen(url).read().decode("utf8")
raw = BeautifulSoup(response, "html.parser").get_text()
tokens = word_tokenize(raw)

mytext = nltk.text.Text(tokens)

lexdiv = len(set(mytext))/len(mytext)


mypdf = open('D:\EasyAccess\911Commission.pdf', mode="rb")


pdf_911 = PyPDF2.PdfFileReader(mypdf)

second = pdf_911.getPage(1)

secondboi = second.extractText()

secondtokens = word_tokenize(secondboi)

secondtextobj = nltk.text.Text(secondtokens)

words = set(secondtextobj, ["9/11", "terrorism", "al", "Qaeda"])

secondlexdiv = len(words)/len(secondtextobj)

print(len(tokens))
print(mytext)
print(lexdiv)
print(secondlexdiv)