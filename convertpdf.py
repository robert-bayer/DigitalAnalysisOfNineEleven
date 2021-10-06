import PyPDF2
import textract
from nltk import word_tokenize

mypdf = open("D:\\EasyAccess\\911Commission.pdf", mode = "rb")


pdf_911 = PyPDF2.PdfFileReader(mypdf)

numP = pdf_911.numPages

txt = ""

txtP = pdf_911.getPage(0)

for i in range(numP):
    txtP = pdf_911.getPage(i)
    txt = txt + txtP.extractText()

print(type(txt))

tokens = word_tokenize(txt)

print(len(tokens))

txt_911 = open("D:\\EasyAccess\\txt_911.txt", mode = "w+")
txt_911.write(txt)

print("done")

