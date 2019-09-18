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

#import feedparser
#llog  = feedparser.parse("http://languagelog.ldc.upenn.edu/nll/?feed=atom")
#print(llog['feed']['title'])
#print(len(llog.enties))
#post = llog.entries[2]
#print(post.title)
#content = post.content[0].value
#print(content[:70])
#nltk.cword_tokenize(nltk.html_clean(content())
#print(nltk.word_tokenize(nltk.clean_html(llog.entries[2].content[0].value)))
##f = open('document.txt')
##raw = f.read()
import os
#os.listdir('.')
#f.read()
#f = open('document.txt', 'rU')
#for line in f:
#    print(line.strip())
#path = nltk.data.find('corpora/gutenberg/melville-moby_dick.txt')
#raw = open(path, 'rU').read()
#s = raw_input("Enter some text:")
#print("You typed", len(nltk.word_tokenize(s)), "words.")
#raw = open('document.txt').read()
#print(type(raw))
#tokens = nltk.word_tokenize(raw)
#print(type(tokens))
#words = [w.lower() for w in tokens]
#print(type(words))
#vocab = sorted(set(words))
#print(type(vocab))
#vocab.append('blog')
## raw.append('blog') # Error
#query = 'Who knows?'
#beatles = ['john', 'paul', 'george', 'ringo']
## print(query + beatles) # Error

#monty = 'Monty Python'
#print(monty)
#circus = "Monty Python's Flying Circus"
#couplet = "Shall I compare thee to a Summer's day?"\
#          "Thou are more lovely and more temperate:"
#print(couplet)
#couplet = ("Rough winds do shake the darling buds of May,"\
#           "And Summer's lease hath all to short a date:")
#print(couplet)
#couplet = """Shall I compare thee to a Summer's day?
#Thou are more lovely and more temperate:"""
#print(couplet)
#print('very'+'very'+'very')
#print('very'*3)
#a = [1,2,3,4,5,6,7,6,5,4,3,2,1]
#b = [' '*2*(7-i)+'very'*i for i in a]
#for line in b:
#    print(line)
#from nltk.corpus import gutenberg
#raw = gutenberg.raw('melville-moby_dick.txt')
#fdist = nltk.FreqDist(ch.lower() for ch in raw if ch.isalpha())
#print(fdist.keys())
#import codecs
#path = nltk.data.find('corpora/unicode_samples/polish-lat2.txt')
#f = codecs.open(path, encoding='latin2')
#for line in f:
#    line = line.strip()
#    print(line.encode('unicode_escape'))
#print(ord('a'))
#print(u'\u0061')
#nacute = u'\u0144'
#print(nacute)
#nacute_utf = nacute.encode('utf8')
#print(repr(nacute_utf))
#import unicodedata
#lines = codecs.open(path, encoding='latin2').readlines()
#line = lines[2]
#print(line.encode('unicode_escape'))
#for c in line:
#    if ord(c) > 127:
#        print('%r U+%04x %s' % (c.encode('utf8'), ord(c), unicodedata.name(c)))
#print(line.find(u'zosta\u0142y'))
#line = line.lower()
#print(line.encode('unicode_escape'))
#import re
#m = re.search(u'\u015b\w*', line)
#print(m.group())
#print(nltk.word_tokenize(line))
#wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]
#print([w for w in wordlist if re.search('en', w)])
#print([w for w in wordlist if re.search('^..j..t..$', w)])
#print([w for w in wordlist if re.search('^[ghi][mno][jlk][def]$', w)])
#chat_words = sorted(set(w for w in nltk.corpus.nps_chat.words()))
#print([w for w in chat_words if re.search('^m+i+n+e+$', w)])
#print([w for w in chat_words if chat_words if re.search('^[ha]+$', w)])
#wsj = sorted(set(nltk.corpus.treebank.words()))
#print([w for w in wsj if re.search('^[0-9]+\.[0-9]+$', w)])
#print([w for w in wsj if re.search('^[A-Z]+\$$', w)])
#print([w for w in wsj if re.search('^[0-9]{4}$', w)])
#print([w for w in wsj if re.search('^[0-9]+-[a-z]{3,5}$', w)])
#print([w for w in wsj if re.search('^[a-z]{5,}-[a-z]{,6}$', w)])
#print([w for w in wsj if re.search('(ed|ing)$', w)])

#word = 'supercalifragilisticexpialidocious'
#print(re.findall(r'[aeiou]', word))
#print(len(re.findall(r'[aeiou]', word)))
#wsj = sorted(set(nltk.corpus.treebank.words()))
#fd = nltk.FreqDist(vs for word in wsj for vs in re.findall(r'[aeiou]{2,}', word))
#print(fd.items())
#regexp = r'^[AEIOUaeiou]+|[AEIOUaeiou]+$|[^AEIOUaeiou]'
#def compress(word):
#    pieces = re.findall(regexp, word)
#    return ''.join(pieces)
#english_udhr = nltk.corpus.udhr.words('English-Latin1')
#print(nltk.tokenwrap(compress(w) for w in english_udhr[:75]))
#rotokas_words = nltk.corpus.toolbox.words('rotokas.dic')
#cvs = [cv for w in rotokas_words for cv in re.findall(r'[ptksvr][aeiou]', w)]
#cfd = nltk.ConditionalFreqDist(cvs)
#cfd.tabulate()
#cv_word_pairs = [(cv, w) for w in rotokas_words for cv in re.findall(r'[ptksvr][aeiou]', w)]
#cv_index = nltk.Index(cv_word_pairs)
#print(cv_index['su'])
#print(cv_index['po'])

#def stem(word):
#    for suffix in ['ing', 'ly', 'ed', 'ious', 'ies', 'ive', 'es', 's', 'ment']:
#        if word.endswith(suffix):
#            return word[:-len(suffix)]
#    return word
#print(re.findall(r'^.*(ing|ly|ed|ious|ies|ive|es|s|ment)$' 'processing'))
#print(re.findall(r'^(.*)(ing|ly|ed|ious|ies|ive|es|s|ment)$' 'processing'))
#print(re.findall(r'^(.*)(ing|ly|ed|ious|ies|ive|es|s|ment)$' 'processes'))
#print(re.findall(r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)$' 'processes'))
#print(re.findall(r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)$' 'language'))
#def stem(word):
#    regexp = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)$'
#    stem, suffix = re.findall(regexp, word)[0]
#    return stem
#raw = """DENNIS: Lsten, strange women lying in ponds distributing swords
#is no basis for a system of government. Supreme executive power derives from
#a mandate from the masses, not from some farcical aquatic ceremony."""
#tokens = nltk.word_tokenize(raw)
#print([stem(t) for t in tokens])
#from nltk.corpus import gutenberg, nps_chat
#moby = nltk.Text(gutenberg.words('melville-moby_dick.txt'))
#print(moby.findall(r"<a>(<.*>)<man>"))
#chat = nltk.Text(nps_chat.words())
#chat.findall(r"<il.*>{3,}")
#from nltk.corpus import brown
#hobbies_learned = nltk.Text(brown.words(categories=['hobbies', 'learned']))
#hobbies_learned.findall(r"<\w*><and><other><\w*s>")
#tokens = nltk.word_tokenize(raw)

#raw = """DENNIS: Lsten, strange women lying in ponds distributing swords
#is no basis for a system of government. Supreme executive power derives from
#a mandate from the masses, not from some farcical aquatic ceremony."""
#porter = nltk.PorterStemmer()
#lancaster = nltk.LancasterStemmer()
#tokens = nltk.word_tokenize(raw)
#print([porter.stem(t) for t in tokens])
#print([lancaster.stem(t) for t in tokens])
#wnl = nltk.WordNetLemmatizer()
#print([wnl.lemmatize(t) for t in tokens])

#raw = """'When I'M a Dunchess,' she said to herself, (not in a very hopeful
#tone though), 'I won't have any pepper in my kitchen AT ALL. Soup does very
#well without--Maybe it's always pepper that makes people that makes people hot-tempered,'..."""
#print(re.split(r' ', raw))
#print(re.split(r'[ \t\n]+', raw))
#print(re.split(r'\W+', raw))
#print(re.findall(r'\W+|\S\w*', raw))
#print(re.findall(r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*", raw))
#text = 'That U.S.A. poster-print costs $12.40...'
#pattern = r'''(?x)
#([A-Z]\.)+
#|\w+(-\w+)*
#|\$?\d+(\.\d+)?%?
#|\.\.\.
#|[][.,;"'?():-_`]
#'''
#print(nltk.regexp_tokenize(text, pattern))

#print(len(nltk.corpus.brown.words())/len(nltk.corpus.brown.sents()))
#sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
#text = nltk.corpus.gutenberg.raw('chesterton-thursday.txt')
#sents = sent_tokenizer.tokenize(text)
#pprint.pprint(sents[171:181])
#def segment(text, segs):
#    words = []
#    last = 0
#    for i in range(len(segs)):
#        if segs[i] == '1':
#            words.append(text[last:i+1])
#            last = i+1
#    words.append(text[last:])
#    return words
#text = "doyouseethekittyseethedoggydoyoulikethekittylikethedoggy"
#seg1 = "0000000000000001000000000010000000000000000100000000000"
#seg2 = "0100100100100001001001000010100100010010000100010010000"
#print(segment(text, seg1))
#print(segment(text, seg2))
#def evaluate(text, segs):
#    words = segment(text, segs)
#    text_size = len(words)
#    lexicon_size = len(' '.join(list(set(words))))
#    return text_size + lexicon_size
##text = "doyouseethekittyseethedoggydoyoulikethekittylikethedoggy"
#seg3 = "0000100100000011001000000110000100010000001100010000001"
#print(segment(text, seg3))
#print(evaluate(text, seg1))
#print(evaluate(text, seg2))
#print(evaluate(text, seg3))
#from random import randint
#def flip(segs, pos):
#    return segs[:pos] + str(1 - int(segs[pos])) + segs[pos+1:]
#def flip_n(segs, n):
#    for i in range(n):
#        segs = flip(segs, randint(0, len(segs) - 1))
#    return segs
#def anneal(text, segs, iterations, cooling_rate):
#    temperature = float(len(segs))
#    while temperature > 0.5:
#        best_segs, best = segs, evaluate(text, segs)
#        for i in range(iterations):
#            guess = flip_n(segs, int(round(temperature)))
#            score = evaluate(text, guess)
#            if score < best:
#                best, best_segs = score, guess
#        score, segs = best, best_segs
#        temperature = temperature / cooling_rate
#        print(evaluate(text, segs), segment(text, segs))
#    print()
#    return segs
#anneal(text, seg1, 5000, 1.2)

silly = ['We', 'called', 'him', 'Tortoise', 'because', 'he', 'taught', 'us', '.']
print(' '.join(silly))
print(';'.join(silly))
print(''.join(silly))
word = 'cat'
sentence = """hello
world"""
print(word)
print(sentence)
fdist = nltk.FreqDist(['dog', 'cat', 'dog', 'cat', 'dog', 'snake', 'dog', 'cat'])
for word in fdist:
    print(word, '->', fdist[word], ';',)
for word in fdist:
    print('%s->%d'%(word, fdist[word]))
template = 'Lee wants a %s right now'
menu = ['sandwich', 'spam fritter', 'pancake']
for snack in menu:
    print(template%snack)
print('%6s'%'dog')
print('%-6s'%'dog')
width = 6
print('%-*s'%(width, 'dog'))
count, total = 3205, 9375
"accuracy for %d words: %2.4f%%" %(total, 100*count/total)
def tabulate(cfdist, words, categories):
    print('%-16s'%'Categories',)
    for word in words:
        print('%6s'%word,)
    print()
    for category in categories:
        print('%-16s'%category, )
        for word in words:
            print('%6d'%cfdist[category][word],)
        print()
from nltk.corpus import brown
cfd = nltk.ConditionalFreqDist(
      (genre, word)
      for genre in brown.categories()
      for word in brown.words(categories=genre)
)
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
print(tabulate(cfd, modals, genres))
output_file = open('output.txt', 'w')
words = set(nltk.corpus.genesis.words('english-kjv.txt'))
for word in sorted(words):
    output_file.write(word+"\n")
print(len(words))
print(str(len(words)))
output_file.write(str(len(words)) + "\n")
output_file.close()
saying = ['After', 'all', 'is', 'said', 'and', 'done', ',', 'more', 'is', 'said', 'than', 'done', '.']
for word in saying:
    print(word, '('+str(len(word))+'),',)
from textwrap import fill
format = '%s (%d),'
pieces = [format % (word, len(word)) for word in saying]
output = ' '.join(pieces)
wrapped = fill(output)
print(wrapped)
