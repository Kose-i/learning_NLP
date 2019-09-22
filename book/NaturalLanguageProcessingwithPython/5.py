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

P204
import nltk

