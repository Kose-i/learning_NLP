
import nltk
#print(nltk.corpus.gutenberg.fileids())

#emma = nltk.corpus.gutenberg.words('austen-emma.txt')
#print(len(emma))

#emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
#emma.concordance('surprize')

from nltk.corpus import gutenberg
#gutenberg.fileids()
#emma = gutenberg.words('austen-emma.txt')

#for fileid in gutenberg.fileids():
#      num_chars = len(gutenberg.raw(fileid))
#      num_words = len(gutenberg.words(fileid))
#      num_sents = len(gutenberg.sents(fileid))
#      num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
#      print(int(num_chars/num_words), int(num_words/num_sents), int(num_words/num_vocab), fileid)

#macbeth_sentences = gutenberg.sents('shakespeare-macbeth.txt')
#print(macbeth_sentences)
#print(macbeth_sentences[1037])
#longest_len = max([len(s) for s in macbeth_sentences])
#print([s for s in macbeth_sentences if len(s)==longest_len])

from nltk.corpus import webtext
#for fileid in webtext.fileids():
#    print(fileid, webtext.raw(fileid)[:65], '...')
#from nltk.corpus import nps_chat
#chatroom = nps_chat.posts('10-19-20s_706posts.xml')
#print(chatroom[123])

from nltk.corpus import brown
#print(brown.categories())
#print(brown.words(categories='news'))
#print(brown.words(fileids=['cg22']))
#print(brown.sents(categories=['news', 'editorial', 'reviews']))
#news_text = brown.words(categories='news')
#fdist = nltk.FreqDist([w.lower() for w in news_text])
#modals = ['can', 'could', 'may', 'might', 'must', 'will']
#for m in modals:
#    print(m+':', fdist[m])
#cfd = nltk.ConditionalFreqDist(
#        (genre, word)
#        for genre in brown.categories()
#        for word in brown.words(categories=genre)
#        )
#genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
#modals = ['can', 'could', 'may', 'might', 'must', 'will']
#cfd.tabulate(conditions=genres, samples=modals)

from nltk.corpus import reuters
#print(reuters.fileids())
#print(reuters.categories())
#print(reuters.categories('training/9865'))
#print(reuters.categories(['training/9865', 'training/9880']))
#print(reuters.fileids('barley'))
#print(reuters.fileids(['barley', 'corn']))
#print(reuters.words('training/9865')[:14])
#print(reuters.words(['training/9865', 'training/9880']))
#print(reuters.words(categories=['barley', 'corn']))

from nltk.corpus import inaugural
#print(inaugural.fileids())
#print([fileid[:4] for fileid in inaugural.fileids()])
#cdf = nltk.ConditionalFreqDist(
#        (target, fileid[:4])
#        for fileid in inaugural.fileids()
#        for w in inaugural.words(fileid)
#        for target in ['america', 'citizen']
#        if w.lower().startswith(target)
#        )
#cdf.plot()

#print(nltk.corpus.cess_esp.words())
#print(nltk.corpus.floresta.words())
#print(nltk.corpus.indian.words('hindi.pos'))
#print(nltk.corpus.udhr.fileids())
#print(nltk.corpus.udhr.words('Javanese-Latin1')[11:])
#from nltk.corpus import udhr
#languages = ['Chickasaw', 'English', 'German_Deutsch', 'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
#cdf = nltk.ConditionalFreqDist(
#        (lang, len(word))
#        for lang in languages
#        for word in udhr.words(lang+'-Latin1')
#        )
#raw_text = nltk.corpus.udhr.raw('Adja-UTF8')
#nltk.FreqDist(raw_text).plot()

#raw = gutenberg.raw("burgess-busterbrown.txt")
#print(raw[1:20])
#words = gutenberg.words("burgess-busterbrown.txt")
#print(words[1:20])
#sents = gutenberg.sents("burgess-busterbrown.txt")
#print(sents[1:20])

from nltk.corpus import PlaintextCorpusReader
#corpus_root = 'usr/share/dict'
#wordlists = PlaintextCorpusReader(corpus_root, '.*')
#print(wordlists.fileids())
#print(wordlists.words('connectives'))

from nltk.corpus import brown
#cdf = nltk.ConditionalFreqDist(
#        (genre, word)
#        for genre in brown.categories()
#        for word in brown.words(categories=genre)
#        )
#genre_word = [(genre, word)
#              for genre in ['news', 'romance']
#              for word in brown.words(categories=genre)
#              ]
#print(len(genre_word))
#print(genre_word)
#cfd = nltk.ConditionalFreqDist(genre_word)
#print(cfd)
#print(cfd.conditions())
#print(cfd['news'])
#print(cfd['romance'])
#print(list(cfd['romance']))
#print(cfd['romance']['could'])

from nltk.corpus import inaugural
#cfd = nltk.ConditionalFreqDist(
#        (target, fileid[:4])
#        for fileid in inaugural.fileids()
#        for w in inaugural.words(fileid)
#        for target in ['america', 'citizen']
#        if w.lower().startswith(target)
#        )
#from nltk.corpus import udhr
#languages = ['Chickasaw', 'English', 'German_Deutsch', 'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
#cfd = nltk.ConditionalFreqDist(
#        (lang, len(word))
#        for lang in languages
#        for word in udhr.words(lang+'-Latin1')
#        )
#cfd.tabulate(conditions=['English', 'German_Deutsch'], samples=range(10), cumulative=True)

#sent = ['In', 'the', 'beginning', 'God', 'created', 'the', 'heaven', 'and', 'the', 'earth', '.']
#print(nltk.bigrams(sent))
#def generate_model(cfdist, word, num=15):
#    for i in range(num):
#        print(word)
#        word = cfdist[word].max()
#text = nltk.corpus.genesis.words('english-kjv.txt')
#bigrams = nltk.bigrams(text)
#cfd = nltk.ConditionalFreqDist(bigrams)
#print(cfd['living'])
#print(generate_model(cfd, 'living'))

#from textproc import plural
#print(plural('with'))

#def unusual_words(text):
#    text_vocab = set(w.lower() for w in text if w.isalpha())
#    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
#    unusual = text_vocab.difference(english_vocab)
#    return sorted(unusual)
#print(unusual_words(nltk.corpus.gutenberg.words('austen-sense.txt')))
from nltk.corpus import stopwords
#print(stopwords.words('english'))
#def content_fraction(text):
#    stopwords = nltk.corpus.stopwords.words('english')
#    content = [w for w in text if w.lower() not in stopwords]
#    return len(content)/len(text)
#print(content_fraction(nltk.corpus.reuters.words()))
#puzzle_letters = nltk.FreqDist('egivrbonl')
#obligatory = 'r'
#wordlist = nltk.corpus.words.words()
#print([w for w in wordlist if len(w)>=6 and obligatory in w and nltk.FreqDist(w)<=puzzle_letters])
#names = nltk.corpus.names
#print(names.fileids())
#male_names   = names.words('male.txt')
#female_names = names.words('female.txt')
#print([w for w in male_names if w in female_names])
#cfd = nltk.ConditionalFreqDist(
#        (fileid, name[-1])
#        for fileid in names.fileids()
#        for name in names.words(fileid)
#        )
#cfd.plot()

#entries = nltk.corpus.cmudict.entries()
#print(len(entries))
#for entry in entries[39943:39951]:
#    print(entry)
#for word, pron in entries:
#    if len(pron) == 3:
#        ph1, ph2, ph3 = pron
#        if ph1 == 'P' and ph3 == 'T':
#            print(word, ph2, end=' ')
#syllable = ['N', 'IHO', 'K', 'S']
#print([word for word, pron in entries if pron[-4:]==syllable ])
#print([w for w, pron in entries if pron[-1] == 'M' and w[-1] == 'n'])
#print(sorted(set(w[:2] for w, pron in entries if pron[0]=='N' and w[0]!='n')))
#def stress(pron):
#    return [char for phone in pron for char in phone if char.isdigit()]
#print([w for w, pron in entries if stress(pron)==['0', '1', '0', '2', '0']])
#print([w for w, pron in entries if stress(pron)==['0', '2', '0', '1', '0']])
#p3 = [(pron[0]+'-'+pron[2],word) for (word, pron) in entries if pron[0]=='P' and len(pron)==3]
#cfd = nltk.ConditionalFreqDist(p3)
#for template in cfd.conditions():
#    if len(cfd[template]) > 10:
#        words = cfd[template].keys()
#        wordlist = ' '.join(words)
#        print(template, wordlist[:70]+'...')
#prondict = nltk.corpus.cmudict.dict()
#print(prondict['fire'])
##print(prondict['blog']) # ERROR
#prondict['blog'] = [['B', 'L', 'AA1', 'G']]
#print(prondict['blog'])
#text = ['natural', 'language', 'processing']
#print([ph for w in text for ph in prondict[w][0]])

#from nltk.corpus import swadesh
#print(swadesh.fileids())
#print(swadesh.words('en'))
#fr2en = swadesh.entries(['fr', 'en'])
#print(fr2en)
#translate = dict(fr2en)
#print(translate['chien'])
#print(translate['jeter'])
#
#de2en = swadesh.entries(['de', 'en'])
#es2en = swadesh.entries(['es', 'en'])
#translate.update(dict(de2en))
#translate.update(dict(es2en))
#print(translate['Hund'])
#print(translate['perro'])
#languages = ['en', 'de', 'nl', 'es', 'fr', 'pt', 'la']
#for i in [139, 140, 141, 142]:
#    print(swadesh.entries(languages)[i])

from nltk.corpus import toolbox
#print(toolbox.entries('rotokas.dic'))

from nltk.corpus import wordnet as wn
#print(wn.synsets('motorcar'))
#print(wn.synset('car.n.01').lemma_names)
#print(wn.synset('car.n.01').definition)
#print(wn.synset('car.n.01').examples)
#print(wn.synset('car.n.01').lemmas)
#print(wn.lemma('car.n.01.automobile'))
#print(wn.lemma('car.n.01.automobile').synset)
#print(wn.lemma('car.n.01.automobile').name)
#print(wn.synsets('car'))
#for synset in wn.synsets('car'):
#    print(synset.lemma_names)
#print(wn.lemmas('car'))

#motorcar = wn.synset('car.n.01')
#types_of_motorcar = motorcar.hyponyms()
#print(types_of_motorcar[26])
##print(sorted(list([lemma.name for synset in types_of_motorcar for lemma in synset.lemmas]))) #TODO ERROR Not Iterable
#print(motorcar.hypernyms())
#paths = motorcar.hypernym_paths()
#print(len(paths))
#print([synset.name for synset in paths[0]])
#print([synset.name for synset in paths[1]])
#print(motorcar.root_hypernyms())

#print(wn.synset('tree.n.01').part_meronyms())
#print(wn.synset('tree.n.01').substance_meronyms())
#print(wn.synset('tree.n.01').member_holonyms())
#for synset in wn.synsets('mint', wn.NOUN):
#    print(str(synset.name)+':'+str(synset.definition))
#print(wn.synset('mint.n.04').part_holonyms())
#print(wn.synset('mint.n.04').substance_holonyms())
#print(wn.synset('mint.n.04').entailments())
#print(wn.synset('eat.v.01').entailments())
#print(wn.synset('tease.v.03').entailments())
#print(wn.lemma('supply.n.02.supply').antonyms())
#print(wn.lemma('rush.v.01.rush').antonyms())
#print(wn.lemma('horizontal.a.01.horizontal').antonyms())
#print(wn.lemma('staccato.r.01.staccato').antonyms())
#print(dir(wn.synset('harmony.n.02')))

#right    = wn.synset('right_whale.n.01')
#orca     = wn.synset('orca.n.01')
#minke    = wn.synset('minke_whale.n.01')
#tortoise = wn.synset('tortoise.n.01')
#novel    = wn.synset('novel.n.01')
#print(right.lowest_common_hypernyms(minke))
#print(right.lowest_common_hypernyms(orca))
#print(right.lowest_common_hypernyms(tortoise))
#print(right.lowest_common_hypernyms(novel))
#print(wn.synset('baleen_whale.n.01').min_depth())
#print(wn.synset('whale.n.02').min_depth())
#print(wn.synset('vertebrate.n.01').min_depth())
#print(wn.synset('entity.n.01').min_depth())
#print(right.path_similarity(minke))
#print(right.path_similarity(orca))
#print(right.path_similarity(tortoise))
#print(right.path_similarity(novel))
