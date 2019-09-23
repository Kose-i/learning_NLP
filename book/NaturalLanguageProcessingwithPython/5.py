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

# P214 Automation Tag
