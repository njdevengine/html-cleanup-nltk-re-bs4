from urllib import request
import nltk, re, pprint
from nltk import word_tokenize
from bs4 import BeautifulSoup

url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
html = request.urlopen(url).read().decode('utf8')

raw = BeautifulSoup(html, 'html.parser').get_text()
tokens = word_tokenize(raw)

#print tokens with appropriate spacing
for i in range(len(tokens)):
    if tokens[i].isalpha() and tokens[i+1].isalpha():
        print(tokens[i], end=" ")
    elif tokens[i].isalpha():
        print(tokens[i], end="")
    else:
        print(tokens[i], end=" ")
