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

P161
