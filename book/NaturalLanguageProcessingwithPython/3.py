from __future__ import division
import nltk, re, pprint

import urllib
#url = "http://www.gutenberg.org/files/2554/2554.html"
#raw = None
#with urllib.request.urlopen(url) as f:
#    raw = f.read()
#print(type(raw))
#print(len(raw))
#print(raw[:75])
#proxies = {'http', 'http://www.someproxy.com:3128'}
#raw = urllib.request.urlopen(url, proxies=proxies).read()
#tokens = nltk.word_tokenize(raw)
#print(type(tokens))
#print(len(tokens))
#print(tokens[:10])
#text = nltk.Text(tokens)
#print(type(text))
#print(text[1020:1060])
#print(raw.find("PART I"))
#print(raw.rfind("End of Project Gutenberg's Crime"))
#raw = raw[5303:1157681]
#print(raw.find("PART I"))

#url = "http://news.bbc.co.uk/2/hi/health/2284783.html"
#html = urllib.request.urlopen(url).read()
#print(html[:60])
#raw = nltk.clean_html(html)
#tokens = nltk.word_tokenize(raw)
#print(tokens)
#tokens = tokens[96:399]
#text = nltk.Text(tokens)
#print(text.concordance('gene'))

