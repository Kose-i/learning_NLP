#foo = ['Monty', 'Python']
#bar = foo
#foo[1] = 'Bodkin'
#print(bar)
#empty = []
#nested = [empty, empty, empty]
#print(nested)
#nested[1].append('Python')
#print(nested)
#nested = [[]] * 3
#nested[1].append('Python')
#nested[1] = ['Monty']
#print(nested)
#size = 5
#python = ['Python']
#snake_nest = [python]*size
#print(snake_nest[0] == snake_nest[1] == snake_nest[2] == snake_nest[3] == snake_nest[4])
#print(snake_nest[0] is snake_nest[1] is snake_nest[2] is snake_nest[3] is snake_nest[4])
#import random
#position = random.choice(range(size))
#snake_nest[position] = ['Python']
#print(snake_nest)
#print(snake_nest[0] == snake_nest[1] == snake_nest[2] == snake_nest[3] == snake_nest[4])
#print(snake_nest[0] is snake_nest[1] is snake_nest[2] is snake_nest[3] is snake_nest[4])
#print([id(snake) for snake in snake_nest])
#mixed = ['cat', '', ['dog'], []]
#for element in mixed:
#    if element:
#        print(element)
#animals = ['cat', 'dog']
#if 'cat' in animals:
#    print('1')
#elif 'dog' in animals:
#    print('2')
#sent = ['No', 'good' 'fish', 'goes', 'anywhere', 'without', 'a', 'porpoise', '.']
#print(all(len(w) > 4 for w in sent))
#print(any(len(w) > 4 for w in sent))

#t = 'walk', 'fem', 3
#print(t)
#print(t[0])
#print(t[1:])
#print(len(t))
#raw = 'I turned off the spectroroute'
#text = ['I', 'turned', 'off', 'the', 'spectroroute']
#pair = (6, 'turned')
#print(raw[2], text[3], pair[1])
#print(raw[-3:], text[-3:], pair[-3:])
#print(len(raw), len(text), len(pair))
#import nltk
#raw = 'Red lorry, yellow lorry, red lorry, yellow lorry.'
#text == nltk.word_tokenize(raw)
#fdist = nltk.FreqDist(text)
#print(list(fdist))
#for key in fdist:
#    print(fdist[key])
#words = ['I', 'turned', 'off', 'the', 'spectroroute']
#words[2], words[3], words[4] = words[3], words[4], words[2]
#print(words)
#tmp = words[2]
#words[2] = words[3]
#words[3] = words[4]
#words[4] = tmp
#tags = ['noun', 'verb', 'prep', 'det', 'noun']
#zip(words, tags)
#print(list(enumerate(words)))
#text = nltk.corpus.nps_chat.words()
#cut = int(0.9*len(text))
#training_data, test_data = text[:cut], text[cut:]
#print(text == training_data + test_data)
#print(len(training_data) / len(test_data))
#words = 'I turned off the spectroroute'.split()
#wordlens = [(len(word), word) for word in words]
#wordlens.sort()
#print(' '.join(w for (_,w) in wordlens))
#lexicon = [
#    ('the', 'det', ['Di:', 'D@']),
#    ('off', 'prep', ['Qf', 'O:f'])
#]
#lexicon.sort()
#lexicon[1] = ('turned', 'VBD', ['t3:nd', 't3`nd'])
#del lexicon[0]
#text = '''"When I use a word," Humpty Dumpty said in rather a scornful tone,
#"it means just what I choose it to mean - neither more nor less."'''
#print([w.lower() for w in nltk.word_tokenize(text)])
#print(max([w.lower() for w in nltk.word_tokenize(text)]))
#print(max(w.lower() for w in nltk.word_tokenize(text)))

#import nltk, re
#from nltk.corpus import brown
#rotokas_words = nltk.corpus.toolbox.words('rotokas.dic')
#cv_word_pairs = [(cv, w) for w in rotokas_words for cv in re.findall('[ptksvr][aeiou]', w)]
#cfd = nltk.ConditionalFreqDist(
#        (genre, word)
#        for genre in brown.categories()
#        for word in brown.words(categories=genre)
#)
#ha_words = ['aaahhhh', 'ah', 'ahah', 'ahahah', 'ahh', 'ahhahahaha', 'ahhh', 'ahhhh', 'ahhhhhh', 'ahhhhhhhhhhhhhh', 'ha', 'haaa', 'hah', 'haha', 'hahaaa', 'hahah' 'hahaha']
#syllables = ['N', 'IHO', 'K', 'S']
#if (len(syllables) > 4 and len(syllables[2]) == 3 and syllables[2][2] in [aeiou] and syllables[2][3] == syllables[1][3]):
#    process(syllables)
#if len(syllables) > 4 and len(syllables[2]) == 3 and syllables[2][2] in [aeiou] and syllables[2][3] == syllables[1][3]:
#    process(syllables)
#tokens = nltk.corpus.brown.words(categories='news')
#count = 0
#total = 0
#for token in tokens:
#    count += 1
#    total += len(token)
#print(total/ count)
#total = sum(len(t) for t in tokens)
#print(total / len(tokens))
#word_list = []
#len_word_list = len(word_list)
#i = 0
#while i < len(tokens):
#    j = 0
#    while j < len_word_list and word_list[j] < tokens[i]:
#        j += 1
#    if j == 0 or tokens[i] != word_list[j]:
#        word_list.insert(j, tokens[i])
#        len_word_list += 1
#    i += 1
#fd = nltk.FreqDist(nltk.corpus.brown.words())
#cumulative = 0.0
#for rank, word in enumerate(fd):
#    cumulative += fd[word]*100 / fd.N()
#    print("%3d %6.2f%% %s" % (rank+1, cumulative, word))
#    if cumulative > 25:
#        break
#text = nltk.corpus.gutenberg.words('milton-paradise.txt')
#longest = ''
#for word in text:
#    if len(word) > len(longest):
#        longest = word
#print(longest)
#maxlen = max(len(word) for word in text)
#print([word for word in text if len(word) == maxlen])
#sent = ['The', 'dog', 'gave', 'John', 'the', 'newspaper']
#n = 3
#print([sent[i:i+n] for i in range(len(sent) - n + 1)])
#m, n = 3, 7
#array = [[set() for i in range(n)] for j in range(m)]
#aray[2][5].add('Alice')
#pprint.pprint(array)
#array = [[set()]*n]*m
#array[2][5].add(7)
#pprint.pprint(array)

#import re, nltk
#def get_text(file):
#    """Read text from a file, normalizing whitespace and stripping HTML markup."""
#    text = open(file).read()
#    text = re.sub('\s+', ' ', text)
#    text = re.sub(r'<.*?>', ' ', text)
#    return text
#help(get_text)
#def repeat(msg, num):
#    return ' '.join([msg]*num)
#monty = 'Monty Python'
#repeat(monty, 3)
#def monty():
#    return "Monty Python"
#print(monty())
#repeat(monty(), 3)
#repeat('Monty Python', 3)
#def tag(word):
#    assert isinstance(word, basestring), "argument to tag() must be a string"
#    if word in ['a', 'the', 'all']:
#        return 'det'
#    else:
#        return 'noun'
#data = nltk.load_corpus()
#results = analyze(data)
#present(results)
#def freq_words(url, freqdist, n):
#    text = nltk.clean_url(url)
#    for word in nltk.word_tokenize(text):
#        freqdist.inc(word.lower())
#    print(freqdist.keys()[:n])
#constitution = "http://www.archives.gov/national-archives-experience"\
#"/charters/constitution_transcript.html"
#fd = nltk.FreqDist()
#print(freq_words(constitution, fd, 20))
#def freq_words(url):
#    freqdist = nltk.FreqDist()
#    text = nltk.clean_url(url)
#    for word in nltk.word_tokenize(text):
#        freqdist.inc(word.lower())
#    return freqdist
#fd = freq_words(constitution)
#print(fd.keys()[:20])
#def accuracy(reference, test):
#    """
#    Calculate the fraction of test items that equal the corresponding reference items.
#
#    Given a list of reference values and a corresponding list of test values,
#    return the fraction of corresponding values that are equal.
#    In particular, return the fraction of indexes
#    {0<i<=len(test)} such that C{test[i] == reference[i]}.
#    >>> accuracy(['ADJ', 'N', 'V', 'N'], ['N', 'N', 'V', 'ADJ'])
#    0.5
#
#    @param reference: An ordered list of reference values.
#    @type reference: C{list}
#    @param test: A list of values to compare against the corresponding refereence values
#    @type test: C{list}
#    @rtype: C{float}
#    @raise ValueError: If C{reference} and C{length} do not have the same length.
#    """
#    
#    if len(reference) != len(test):
#        raise ValueError("Lists must have the same length.")
#    num_correct = 0
#    for x, y in izip(reference, test):
#        if x == y:
#            num_correct += 1
#    return float(num_correct) / len(reference)

#import nltk
#from functools import cmp_to_key
#sent = ['Take', 'care', 'of', 'the', 'sense', ',', 'and', 'the', 'sounds', 'will', 'take', 'care', 'of', 'themselves', '.']
#def extract_property(prop):
#    return [prop(word) for word in sent]
#print(extract_property(len))
#def last_letter(word):
#    return word[-1]
#print(extract_property(last_letter))
#print(extract_property(lambda w : w[0]))
#print(sorted(sent))
#def Cmp(a, b):
#    return a > b
#print(sorted(sent, key=cmp_to_key(Cmp)))
#print(sorted(sent, key=cmp_to_key(lambda x,y: Cmp(len(y), len(x)))))
#def search1(substring, words):
#    result = []
#    for word in words:
#        if substring in word:
#            result.append(word)
#    return result
#def search2(substring, words):
#    for word in words:
#        if substring in word:
#            yield word
#print("search")
#for item in search1('zz', nltk.corpus.brown.words()):
#    print(item)
#for item in search2('zz', nltk.corpus.brown.words()):
#    print(item)
#def permutations(seq):
#    if len(seq) <= 1:
#        yield seq
#    else:
#        for perm in permutations(seq[1:]):
#            for i in range(len(perm) +1):
#                yield perm[:i] + seq[0:1] + perm[i:]
#print(list(permutations(['police', 'fish', 'buffalo'])))
#def is_content_word(word):
#    return word.lower() not in ['a', 'of', 'the', 'and', 'will', ',', '.']
#sent = ['Take', 'care', 'of', 'the', 'sense', ',', 'and', 'the', 'sounds', 'will', 'take', 'care', 'of', 'themselves', '.']
#print(filter(is_content_word, sent))
#print([w for w in sent if is_content_word(w)])
#lengths = map(len, nltk.corpus.brown.sents(categories='news'))
#print(sum(list(lengths)) / len(list(lengths)))
#lengths = [len(w) for w in nltk.corpus.brown.sents(categories='news')]
#print(sum(lengths) / len(lengths))
#print(map(lambda w: len(filter(lambda c: c.lower() in "aeiou", w)), sent))
#print([len([c for c in w if c.lower() in "aeiou"]) for w in sent])
#def repeat(msg='<empty>', num=1):
#    return msg*num
#print(repeat(msg='Alice'))
#print(repeat(num=5, msg='Alice'))
#def generic(*args ,**kwargs):
#    print(args)
#    print(kwargs)
#generic(1, "African swallow", monty="python")
#song = [
#    ['four', 'calling', 'birds'],
#    ['three', 'French', 'hens'],
#    ['two', 'turtle', 'doves']
#]
#zip(song[0], song[1], song[2])
#zip(*song)
#def freq_words(file, min=1, num=10):
#    text = open(file).read()
#    tokens = nltk.word_tokenize(text)
#    freqdist = nltk.FreqDist(t for t in tokens if len(t)>=min)
#    return freqdist.keys()[:num]
#fw = freq_words('ch01.rst', 4, 10)
#fw = freq_words('ch01.rst', min=4, num=10)
#fw = freq_words('ch01.rst',  num=10, min=4)
#def freq_words(file, min=1, num=10, verbose=False):
#    freqdist = FreqDist()
#    if verbose : print("Opening"), file
#    text = open(file).read()
#    if verbose: print("Read in %d characters"%len(file))
#    for word in nltk.word_tokenize(text):
#        if len(word) >= min:
#            freqdist.inc(word)
#            if verbose and freqdist.N() % 100 == 0:print(".")
#    if verbose:print()
#    return freqdist.keys()[:num]

#import nltk
##print(nltk.metrics.distance)
#def find_words(text, wordlength, result=[]):
#    for word in text:
#        if len(word) == wordlength:
#            result.append(word)
#    return result
#print(find_words(['omg', 'teh', 'lolcat', 'sitted', 'on', 'teh', 'mat'], 3))
#print(find_words(['omg', 'teh', 'lolcat', 'sitted', 'on', 'teh', 'mat'], 2, ['ur']))
#print(find_words(['omg', 'teh', 'lolcat', 'sitted', 'on', 'teh', 'mat'], 3))
#import pdb
#print(find_words(['cat'], 3))
#pdb.run("find_words(['dog'], 3)")

#import nltk, pprint, re
#def factorial1(n):
#    result = 1
#    for i in range(n):
#        result *= (i+1)
#    return result
#def factorial2(n):
#    if n == 1:
#        return 1
#    else:
#        return n*factorial2(n-1)
#def size1(s):
#    return 1+sum(size1(child) for child in s.hyponyms())
#def size2(s):
#    layer = [s]
#    total = 0
#    while layer:
#        total += len(layer)
#        layer = [h for c in layer for h in c.hyponyms()]
#    return total
#from nltk.corpus import wordnet as wn
#dog = wn.synset('dog.n.01')
#print(size1(dog))
#print(size2(dog))
#def insert(trie, key, value):
#    if key:
#        first, rest = key[0], key[1:]
#        if first not in trie:
#            trie[first] = {}
#        insert(trie[first], rest, value)
#    else:
#        trie['value'] = value
#trie = nltk.defaultdict(dict)
#insert(trie, 'chat', 'cat')
#insert(trie, 'chien', 'dog')
#insert(trie, 'chair', 'flesh')
#insert(trie, 'chaic', 'stylish')
#trie = dict(trie) # for nicher printing
#print(trie['c']['h']['a']['t']['value'])
#pprint.pprint(trie)
#def raw(file):
#    contents = open(file).read()
#    contents = re.sub(r'<.*?>', ' ', contents)
#    contents = re.sub('\s+', ' ', contents)
#    return contents
#def snippet(doc, term): # buggy
#    text = ' '*30 + raw(doc) + ' '*30
#    pos = text.index(term)
#    return text[pos-30:pos+30]
#print("Building Index...")
#files = nltk.corpus.movie_reviews.abspaths()
#idx = nltk.Index((w, f) for f in files for w in raw(f).split())
#query = ''
#while query != "quit":
#    query = input("query> ")
#    if query in idx:
#        for doc in idx[query]:
#            print(snippet(doc, query))
#    else:
#        print("Not found")
#def preprocess(tagged_corpus):
#    words = set()
#    tags = set()
#    for sent in tagged_corpus:
#        for word, tag in sent:
#            words.add(word)
#            tags.add(tag)
#    wm = dict((w,i) for (i,w) in enumerate(words))
#    tm = dict((t,i) for (i,t) in enumerate(tags))
#    return [[(wm[w], tm[t]) for (w,t) in sent] for sent in tagged_corpus]
#from timeit import Timer
#vocab_size = 100000
#setup_list = "import random; vocab = range(%d)" % vocab_size
#setup_set  = "import random; vocab = set(range(%d))" % vocab_size
#statement = "random.randint(0, %d) in vocab" % vocab_size*2
#print(Timer(statement, setup_list).timeit(1000))
#print(Timer(statement, setup_set ).timeit(1000))
#def virahanka1(n):
#    if n == 0:
#        return [""]
#    elif n == 1:
#        return ["S"]
#    else:
#        s = ["S" + prosody for prosody in lookup[n-1]]
#        l = ["L" + prosody for prosody in lookup[n-2]]
#        return s+l
#def virahanka2(n):
#    lookup = [[""], ["S"]]
#    for i in range(n-1):
#        s = ["S" + prosody for prosody in lookup[i+1]]
#        l = ["L" + prosody for prosody in lookup[i]]
#        lookup.append(s+l)
#    return lookup[n]
#def virahanka3(n, lookup={0:[""], 1:["S"]}):
#    if n not in lookup:
#        s = ["S" + prosody for prosody in lookup[i+1]]
#        l = ["L" + prosody for prosody in lookup[i]]
#        lookup[n] = s+l
#    return lookup[n]
#from nltk import memoize
#@memoize
#def virahanka4(n):
#    if n == 0:
#        return [""]
#    elif n == 1:
#        return ["S"]
#    else:
#        s = ["S" + prosody for prosody in virahanka4(n-1)]
#        l = ["L" + prosody for prosody in virahanka4(n-2)]
#        return s+l
#print(virahanka1(4))
#print(virahanka2(4))
#print(virahanka3(4))
#print(virahanka4(4))

import nltk, pylab, matplotlib
colors = 'rgbcmyk' # Red, Green, Blue, Magenta, Yellow, Black
def bar_chart(categories, words, counts):
    "Plot a bar chart showing counts for each word by category"
    ind = pylab.arange(len(words))
    width = 1/ (len(categories) + 1)
    bar_groups = []
    for c in range(len(categories)):
        bars = pylab.bar(ind+c*width, counts[categories[c]], width, color=colors[c % len(colors)])
        bar_groups.append(bars)
        pylab.xticks(ind+width, words)
        pylab.ylabel('Freqency')
        pylab.legend([b[0] for b in bar_groups], categories, loc='upper left')
        pylab.title('Freqency of Six Verbs by Genre')
        pylab.show()
genres = ['news', 'religion', 'hobbies', 'government', 'adventure']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
cfdist = nltk.ConditionalFreqDist(
            (genre, word)
            for genre in genres
            for word in nltk.corpus.brown.words(categories=genre)
            if word in modals
)
counts = {}
for genre in genres:
    counts[genre] = [cfdist[genre][word] for word in modals]
bar_chart(genres, modals, counts)
matplotlib.use('Agg')
pylab.savefig('modals.png')
print('Content-Type: text/html')
print()
print('<html><body>')
print('<img src="modals.png"/>')
print('</body></html>')
