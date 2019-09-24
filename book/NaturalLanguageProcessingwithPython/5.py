#import nltk
#text = nltk.word_tokenize("And now for something completely different")
#print(nltk.pos_tag(text))
#nltk.help.upenn_tagset('RB')
#text = nltk.word_tokenize("They refuse to permit us to obtain the refuse permit")
#print(nltk.pos_tag(text))
#text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
#text.similar('woman')
#text.similar('bought')
#text.similar('over')
#text.similar('the')

#import nltk
#tagged_token = nltk.tag.str2tuple('fly/NN')
#print(tagged_token)
#print(tagged_token[0])
#print(tagged_token[1])
#sent = """
#The/AT grand/JJ jury/NN commented/VED on/IN a/AT number/NN of/IN
#other/AP topics/NNS ,/, AMONG/IN them/PPO the/AT Atlanta/NP and/CC
#Fulton/NP-tl County/NN-tl prchasing/VBG departments/NNS which/WDT it/PPS
#said/VBD ``/`` ARE/BER well/QL operated/VBN and/CC follow/VB generally/RB
#accepted/VBN of/IN both/ABX governments/NNS ''/'' ./.
#"""
#print([nltk.tag.str2tuple(t) for t in sent.split()])
#print(nltk.corpus.brown.tagged_words())
#print(nltk.corpus.brown.tagged_words())
#print(nltk.corpus.nps_chat.tagged_words())
#print(nltk.corpus.conll2000.tagged_words())
#print(nltk.corpus.treebank.tagged_words())
#print(nltk.corpus.brown.tagged_words())
#print(nltk.corpus.treebank.tagged_words())
#print(nltk.corpus.sinica_treebank.tagged_words)
#print(nltk.corpus.indian.tagged_words())
#print(nltk.corpus.mac_morpho.tagged_words())
#print(nltk.corpus.conll2002.tagged_words())
#print(nltk.corpus.cess_cat.tagged_words())
#from nltk.corpus import brown
#brown_news_tagged = brown.tagged_words(categories='news')
#tag_fd = nltk.FreqDist(tag for (word, tag) in brown_news_tagged)
#print(tag_fd.keys())
#word_tag_pairs = nltk.bigrams(brown_news_tagged)
#print(list(nltk.FreqDist(a[1] for (a,b) in word_tag_pairs if b[1] == 'N')))
#wsj = nltk.corpus.treebank.tagged_words()
#word_tag_fd = nltk.FreqDist(wsj)
#print([word + "/" + tag for (word, tag) in word_tag_fd if tag.startswith('V')])
#cfd1 = nltk.ConditionalFreqDist(wsj)
#print(cfd1['yield'].keys())
#print(cfd1['cut'].keys())
#cfd2 = nltk.ConditionalFreqDist((tag, word) for (word, tag) in wsj)
#print(cfd2['VN'].keys())
#print([w for w in cfd1.conditions() if 'VD' in cfd1[w] and 'VN' in cfd1[w]])
#idx1 = wsj.index(('kicked', 'VD'))
#print(wsj[idx1 - 4:idx1 + 1])
#idx2 = wsj.index(('kicked', 'VN'))
#print(wsj[idx2 - 4:idx2 + 1])
#def findtags(tag_prefix, tagged_text):
#    cfd = nltk.CondtionalFreqDist((tag, word) for (word, tag) in tagged_text if tag.startswith(tag_prefix))
#    return dict((tag, cfd[tag].keys()[:5]) for tag in cfd.conditions())
#tagdict = findtags('NN', nltk.corpus.brown.tagged_words(categories='news'))
#for tag in sorted(tagdict):
#    print(tag, tagdict[tag])
#brown_learned_text = brown.words(categories='learned')
#print(sorted(set(b for (a,b) in nltk.ibigrams(brown_learned_text) if a=='often')))
#brown_lrnd_tagged = brown.tagged_words(categories='learned', simplify_tags=True)
#tags = [b[1] for (a,b) in nltk.ibigrams(brown_lrnd_tagged) if a[0]=='often']
#fd = nltk.FreqDist(tags)
#fd.tabulate()
#def process(sentence):
#    for (w1, t1), (w2, t2), (w3, t3) in nltk.trigrams(sentence):
#        if (t1.startswith('V') and t2=='TO' and t3.startswith('V')):
#            print(w1, w2, w3)
#for tagged_sent in brown.tagged_sents():
#    process(tagged_sent)
#brown_news_tagged = brown.tagged_words(categories='news')
#data = nltk.ConditionalFreqDist((word.lower(), tag) for (word, tag) in brown_news_tagged)
#for word in data.conditions():
#    if len(data[word]) > 3:
#        tags = data[word].keys()
#        print(word, ' '.join(tags))

#import nltk
#pos = {}
#print(pos)
#pos['colorless'] = 'ADJ'
#print(pos)
#pos['ideas'] = 'NN'
#pos['sleep'] = 'V'
#pos['furiously'] = 'ADJ'
#print(pos)
#print(pos['ideas'])
##print(pos['green']) # KeyERROR
#print(list(pos))
#print(sorted(pos))
#print([w for w in pos if w.endswith('s')])
#for word in sorted(pos):
#    print(word + ":" + pos[word])
#print(pos.keys())
#print(pos.values())
#print(pos.items())
#for key, val in sorted(pos.items()):
#    print(key+":"+val)
#pos = {'colorless':'ADJ', 'ideas':'N', 'furiously':'ADJ'}
#pos = dict(colorless='ADJ', ideas='N', furiously='ADJ')
##pos = {['ideas', 'blogs', 'adventures']: 'N'} # TypeERROR
#frequency = nltk.defaultdict(int)
#frequency['colorless'] = 4
#print(frequency['ideas'])
#pos = nltk.defaultdict(list)
#pos['sleep'] = ['N', 'V']
#print(pos['ideas'])
#pos = nltk.defaultdict(lambda: 'N')
#pos['colorless'] = 'ADJ'
#print(pos['blog'])
#print(pos.items())
#f = lambda: 'N'
#print(f())
#def g(): # Similar f()
#    return 'N'
#print(g())
#alice = nltk.corpus.gutenberg.words('carroll-alice.txt')
#vocab = nltk.FreqDist(alice)
#v1000 = list(vocab)[:1000]
#mapping = nltk.defaultdict(lambda: 'UNK')
#for v in v1000:
#    mapping[v] = v
#alice2 = [mapping[v] for v in alice]
#print(alice2[:100])
#counts = nltk.defaultdict(int)
#from nltk.corpus import brown
#for (word, tag) in brown.tagged_words(categories='news'):
#    counts[tag] += 1
#print(counts['N'])
#print(list(counts))
#from operator import itemgetter
#print(sorted(counts.items(), key=itemgetter(1), reverse=True))
#print([t for t, c in sorted(counts.items(), key=itemgetter(1), reverse=True)])
#pair = ('NP', 8336)
#print(pair[1])
#print(itemgetter(1)(pair))
#last_letters = nltk.defaultdict(list)
#words = nltk.corpus.words.words('en')
#for word in words:
#      key = word[-2:]
#      last_letters[key].append(word)
#print(last_letters['ly'])
#print(last_letters['zy'])
#anagrams = nltk.defaultdict(list)
#for word in words:
#    key = ''.join(sorted(word))
#    anagrams[key].append(word)
#print(anagrams['aeilnrt'])
#anagrams = nltk.Index((''.join(sorted(w)), w) for w in words)
#pos = nltk.defaultdict(lambda: nltk.defaultdict(int))
#brown_news_tagged = brown.tagged_words(categories='news')
#for ((w1, t1), (w2, t2)) in nltk.bigrams(brown_news_tagged):
#    pos[(t1, w2)][t2] += 1
#print(pos[('DET', 'right')])
#counts = nltk.defaultdict(int)
#for wrod in nltk.corpus.gutenberg.words('milton-paradise.txt'):
#    counts[word] += 1
#print([key for (key, value) in counts.items() if value==32])
#pos = {'colorless':'ADJ', 'ideas':'N', 'sleep':'V', 'furiously':'ADJ'}
#pos2 = dict((value, key) for (key, value) in pos.items())
#print(pos2['N'])
#pos.update({'cats':'N', 'scratch':'V', 'peacefully':'ADV', 'old':'ADJ'})
#pos2 = nltk.defaultdict(list)
#for key, value in pos.items():
#    pos2[value].append(key)
#print(pos2['ADJ'])

#import nltk
#from nltk.corpus import brown
#brown_tagged_sents = brown.tagged_sents(categories='news')
#brown_sents = brown.sents(categories='news')
#tags = [tag for (word, tag) in brown.tagged_words(categories='news')]
#print(nltk.FreqDist(tags).max())
#raw = 'I do not like green eggs and ham, I do not like them Sam I am!'
#tokens = nltk.word_tokenize(raw)
#default_tagger = nltk.DefaultTagger('NN')
#print(default_tagger.tag(tokens))
#print(default_tagger.evaluate(brown_tagged_sents))
#patterns = [
#      (r'.*ing$',               'VBG'),
#      (r'.*ed$',                'VBD'),
#      (r'.*es$',                'VBZ'),
#      (r'.*ould$',              'MD'),
#      (r'.*\'s$',               'NN$'),
#      (r'.*s$',                 'MNS'),
#      (r'.^-?[0-9]+(.[0-9]+)?$','CD'),
#      (r'.*',                   'NN')
#    ]
#regexp_tagger = nltk.RegexpTagger(patterns)
#print(regexp_tagger.tag(brown_sents[3]))
#print(regexp_tagger.evaluate(brown_tagged_sents))
#fd = nltk.FreqDist(brown.words(categories='news'))
#cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
#most_freq_words = list(fd.keys())[:100]
#likely_tags = dict((word, cfd[word].max()) for word in most_freq_words)
#baseline_tagger = nltk.UnigramTagger(model=likely_tags)
#print(baseline_tagger.evaluate(brown_tagged_sents))
#sent = brown.sents(categories='news')[3]
#print(baseline_tagger.tag(sent))
#baseline_tagger = nltk.UnigramTagger(model=likely_tags, backoff=nltk.DefaultTagger('NN'))
#def performance(cfd, wordlist):
#    lt = dict((word, cfd[word].max()) for word in wordlist)
#    baseline_tagger = nltk.UnigramTagger(model=lt, backoff=nltk.DefaultTagger('NN'))
#    return baseline_tagger.evaluate(brown.tagged_sents(categories='news'))
#def display():
#    import pylab
#    words_by_freq = list(nltk.FreqDist(brown.words(categories='news')))
#    cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
#    sizes = 2 ** pylab.arange(15)
#    perfs = [performance(cfd, words_by_freq[:size]) for size in sizes]
#    pylab.plot(sizes, perfs, '-bo')
#    pylab.title('Lookup Tagger Performance with Varying Model Size')
#    pylab.xlabel('Model Size')
#    pylab.ylabel('Performance')
#    pylab.show()
#display()

#import nltk
#from nltk.corpus import brown
#brown_tagged_sents = brown.tagged_sents(categories='news')
#brown_sents = brown.sents(categories='news')
#unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
#print(unigram_tagger.tag(brown_sents[2007]))
#print(unigram_tagger.evaluate(brown_tagged_sents))
#size = int(len(brown_tagged_sents) * 0.9)
#print(size)
#train_sents = brown_tagged_sents[:size]
#test_sents = brown_tagged_sents[size:]
#unigram_tagger = nltk.UnigramTagger(train_sents)
#print(unigram_tagger.evaluate(test_sents))
#bigram_tagger = nltk.BigramTagger(train_sents)
#print(bigram_tagger.tag(brown_sents[2007]))
#unseen_sent = brown_sents[4203]
#print(bigram_tagger.tag(unseen_sent))
#print(bigram_tagger.evaluate(test_sents))
#t0 = nltk.DefaultTagger('NN')
#t1 = nltk.UnigramTagger(train_sents, backoff=t0)
#t2 = nltk.BigramTagger(train_sents, backoff=t1)
#print(t2.evaluate(test_sents))
#from pickle import dump
#output = open('t2.pkl', 'wb')
#output.close()
#from pickle import load
#input = open('t2.pkl', 'rb')
#tagger = load(input)
#input.close()
#text = """The board's action shows what free enterprise
#is up against in our complex maze of regulaory laws ."""
#tokens = text.split()
#print(tagger.tag(tokens))
#cfd = nltk.ConditionalFreqDist(
#            ((x[1], y[1], z[0]), z[1])
#            for sent in brown_tagged_sents
#            for x, y, z in nltk.trigrams(sent)
#)
#ambiguous_contexts = [c for c in cfd.conditions() if len(cfd[c]) > 1]
#print(sum(cfd[c].N() for c in ambiguous_contexts) / cfd.N())
#test_tags = [tag for sent in brown.sents(categories='editorial') for (word, tag) in t2.tag(sent)]
#gold_tags = [tag for (word, tag) in brown.tagged_words(categories='editorial')]
#print(nltk.ConfusionMatrix(gold, test))
#brown_tagged_sents = brown.tagged_sents(categories='news')
#brown_sents = brown.sents(categories='news')
#size = int(len(brown_tagged_sents)*0.9)
#train_sents = brown_tagged_sents[:size]
#test_sents = brown_tagged_sents[size:]
#t0 = nltk.DefaultTagger('NN')
#t1 = nltk.UnigramTagger(train_sents, backoff=t0)
#t2 = nltk.BigramTagger(train_sents, backoff=t1)
#print(t2.evaluate(test_sents))
#nltk.tag.brill.demo()
#print(open("errors.out").read())
