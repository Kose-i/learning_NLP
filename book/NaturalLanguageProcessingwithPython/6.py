#import nltk
#def gender_features(word):
#    return {'last_letter': word[-1]}
#print(gender_features('Shrek'))
#from nltk.corpus import names
#import random
#names = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')])
#random.shuffle(names)
#featuresets = [(gender_features(n), g) for (n,g) in names]
#train_set, test_set = featuresets[500:], featuresets[:500]
#classifier = nltk.NaiveBayesClassifier.train(train_set)
#print(classifier.classify(gender_features('Neo')))
#print(classifier.classify(gender_features('Trinity')))
#print(nltk.classify.accuracy(classifier, test_set))
#classifier.show_most_informative_features(5)
#from nltk.classify import apply_features
#train_set = apply_features(gender_features, names[500:])
#test_set  = apply_features(gender_features, names[:500])
#def gender_features2(name):
#    features ={}
#    features["firstletter"] = name[0].lower()
#    features["lastletter"]  = name[-1].lower()
#    for letter in 'abcdefghijklmnopqrstuvwxyz':
#        features["count(%s)"% letter] = name.lower().count(letter)
#        features["has(%s)"% letter]  = (letter in name.lower())
#    return features
#print(gender_features2('John'))
#featuresets = [(gender_features2(n), g) for (n,g) in names]
#trainset, test_set = featuresets[500:], featuresets[:500]
#classifier = nltk.NaiveBayesClassifier.train(train_set)
#print(nltk.classify.accuracy(classifier, test_set))
#train_names   = names[1500:]
#devtest_names = names[500:1500]
#test_names    = names[:500]
#train_set   = [(gender_features(n), g) for (n,g) in train_names]
#devtest_set = [(gender_features(n), g) for (n,g) in devtest_names]
#test_set    = [(gender_features(n), g) for (n,g) in test_names]
#classifier = nltk.NaiveBayesClassifier.train(train_set)
#print(nltk.classify.accuracy(classifier, devtest_set))
#errors = []
#for (name, tag) in devtest_names:
#    guess = classifier.classify(gender_features(name))
#    if guess != tag:
#        errors.append( (tag, guess, name) )
#for (tag, guess, name) in sorted(errors): # doctest: +ELLIPSIS
#    print('correct=%-8s guess=%-8s name=%-30s'% (tag, guess, name))
#def gender_features(word):
#    return {'suffix1': word[-1:], 'suffix2': word[-2:]}
#train_set   = [(gender_features(n), g) for (n,g) in train_names]
#devtest_set = [(gender_features(n), g) for (n,g) in devtest_names]
#classifier = nltk.NaiveBayesClassifier.train(train_set)
#print(nltk.classify.accuracy(classifier, devtest_set))
#from nltk.corpus import movie_reviews
#documents = [(list(movie_reviews.words(fileid)), category)
#              for category in movie_reviews.categories()
#              for fileid in movie_reviews.fileids(category)
#]
#all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
#word_features = list(all_words.keys())[:2000]
#def document_features(document):
#    document_words = set(document)
#    features = {}
#    for word in word_features:
#        features['contains(%s)'% word] = (word in document_words)
#    return features
#print(document_features(movie_reviews.words('pos/cv957_8737.txt')))
#featuresets = [(document_features(d), c) for (d,c) in documents]
#train_set, test_set = featuresets[100:], featuresets[:100]
#classifier = nltk.NaiveBayesClassifier.train(train_set)
#print(nltk.classify.accuracy(classifier, test_set))
#classifier.show_most_informative_features(5)
#from nltk.corpus import brown
#suffix_fdist = nltk.FreqDist()
#for word in brown.words():
#    word = word.lower()
#    suffix_fdist[word[-1:]] += 1
#    suffix_fdist[word[-2:]] += 1
#    suffix_fdist[word[-3:]] += 1
#    #suffix_fdist.inc(word[-1:])
#    #suffix_fdist.inc(word[-2:])
#    #suffix_fdist.inc(word[-3:])
#common_suffixes = list(suffix_fdist.keys())[:100]
#print(common_suffixes)
#def pos_features(word):
#    features = {}
#    for suffix in common_suffixes:
#        features['endswith(%s)'% suffix] = word.lower().endswith(suffix)
#    return features
#tagged_words = brown.tagged_words(categories='news')
#featuresets = [(pos_features(n), g) for (n,g) in tagged_words]
#size = int(len(featuresets) * 0.1)
#train_set, test_set = featuresets[size:], featuresets[:size]
#classifier = nltk.DecisionTreeClassifier.train(train_set)
#print(nltk.classify.accuracy(classifier, test_set))
#print(classifier.classify(pos_features('cats')))
#print(classifier.pseudocode(depth=4))
#def pos_features(sentence, i):
#    features = {"suffix(1)": sentence[i][-1:],
#                "suffix(2)": sentence[i][-2:],
#                "suffix(3)": sentence[i][-3:]
#    }
#    if i == 0:
#        features["prev-word"] = "<START>"
#    else:
#        features["prev-word"] = sentence[i - 1]
#    return features
#print(pos_features(brown.sents()[0], 8))
#tagged_sents = brown.tagged_sents(categories='news')
#featuresets = []
#for tagged_sent in tagged_sents:
#    untagged_sent = nltk.tag.untag(tagged_sent)
#    for i, (word, tag) in enumerate(tagged_sent):
#        featuresets.append((pos_features(untagged_setn, i), tag))
#size = int(len(featuresets) * 0.1)
#train_set, test_set = featuresetes[size:], featuresets[:size]
#classifier = nltk.NaiveBayesClassifier.train(train_set)
#print(nltk.classify.accuracy(classifier, test_set))
#def pos_features(sentence, i, history):
#    features = {"suffix(1)": sentence[i][-1:],
#                "suffix(2)": sentence[i][-2:],
#                "suffix(3)": sentence[i][-3:]
#    }
#    if i == 0:
#        features["prev-word"] = "<START>"
#        features["prev-tag"]  = "<START>"
#    else:
#        features["prev-word"] = sentence[i - 1]
#        features["prev-tag"]  = history[i - 1]
#    return features
#class ConsecutivePosTagger(nltk.TaggerI):
#    def __init__(self, train_sents):
#        train_set = []
#        for tagged_sent in train_sents:
#            untagged_sent = nltk.tag.untag(tagged_setn)
#            featureset = pos_features(untagged_sent, i, history)
#            train_set.append((featureset, tag))
#            history.append(tag)
#        self.classifier = nltk.NaiveBayesClassifier.train(train_set)
#    def tag(self, sentence):
#        history = []
#        for i, word in enumerate(sentence):
#            featureset = pos_features(sentence, i, history)
#            tag = self.classifier.classify(featureset)
#            hisotyr.append(tag)
#        return zip(sentence, history)
#tagged_sents = brown.tagged_sents(categories='news')
#size = int(len(tagged_sents) * 0.1)
#train_sents , test_sents = tagged_sents[size:], tagged_sents[:size]
#tagger = ConsecutivePosTagger(train_sents)
#print(tagger.evaluate(test_sents))

#import nltk
#sents = nltk.corpus.treebank_raw.sents()
#tokens = []
#boundaries = set()
#offset = 0
#for sent in nltk.corpus.treebank_raw.sents():
#    tokens.extend(sent)
#    offset += len(sent)
#    boundaries.add(offset-1)
#def punct_features(tokens, i):
#    return {'next-word-capitalized': tokens[i+1][0].isupper(),
#            'prevword': tokens[i-1].lower(),
#            'punct': tokens[i],
#            'prev-word-is-one-char': len(tokens[i - 1]) == 1}
#featuresets = [(punct_features(tokens, i), (i in boundaries))
#                for i in range(1, len(tokens)-1)
#                if tokens[i] in '.?!']
#size = int(len(featuresets) * 0.1)
#train_set, test_set = featuresets[size:], featuresets[:size]
#classifier = nltk.NaiveBayesClassifier.train(train_set)
#print(nltk.classify.accuracy(classifier, test_set))
#def segment_sentences(words):
#    start = 0
#    sents = []
#    for i, word in enumerate(words):
#        if word in '.?!' and classifier.classify(punct_features(words, i)) == True:
#            sents.apppend(words[start:i+1])
#            start = i+1
#    if start < len(words):
#        sents.append(words[start:])
#    return sents
#posts = nltk.corpus.nps_chat.xml_posts()[:10000]
#def dialogue_act_features(post):
#    features = {}
#    for word in nltk.word_tokenize(post):
#        features['contains(%s)'% word.lower()] = True
#    return features
#featuresets = [(dialogue_act_features(post.text), post.get('class')) for post in posts]
#size = int(len(featuresets)*0.1)
#train_set, test_set = featuresets[size:], featuresets[:size]
#classifier = nltk.NaiveBayesClassifier.train(train_set)
#print(nltk.classify.accuracy(classifier, test_set))
#def rte_features(rtepair):
#    extractor = nltk.RTEFeatureExtractor(rtepair)
#    features = {}
#    features['word_overlap']   = len(extractor.overlap('word'))
#    features['word_hyp_extra'] = len(extractor.hyp_extra('word'))
#    features['ne_overlap']     = len(extractor.overlap('ne'))
#    features['ne_hyp_extra']   = len(extractor.hyp_extra('ne'))
#    return features
#rtepair = nltk.corpus.rte.pairs(['rte3_dev.xml'])[33]
#extractor = nltk.RTEFeatureExtractor(rtepair)
#print(extractor.text_words)
#print(extractor.hyp_words)
#print(extractor.overlap('ne'))
#print(extractor.hyp_extra('word'))
#import random
#from nltk.corpus import brown
#tagged_sents = list(brown.tagged_sents(categories='news'))
#random.shuffle(tagged_sents)
#size = int(len(tagged_sents)*0.3)
#train_set, test_set = featuresets[size:], featuresets[:size]
#file_ids = brown.fileids(categories='news')
#size = int(len(file_ids)*0.1)
#train_set = brown.tagged_sents(file_ids[size:])
#test_set  = brown.tagged_sents(file_ids[:size])
#train_set = brown.tagged_sents(categories='news')
#test_set  = brown.tagged_sents(categories='fiction')
#classifier = nltk.NaiveBayesClassifier.train(train_set)
#print('Accuracy: %4.2f'% nltk.classify.accuracy(classifier, test_set))
#def tag_list(tagged_sents):
#    return [tag for sent in tagged_sents for (word, tag) in sent]
#def apply_tagger(tagger, corpus):
#    return [tagger.tag(nltk.tag.untag(sent)) for sent in corpus]
#gold = tag_list(brown.tagged_sents(categories='editorial'))
#test = tag_list(apply_tagger(t2, brown.tagged_sents(categories='editorial')))
#cm = nltk.ConfusionMatrix(gold, test)

import nltk
import math
def entropy(labels):
    freqdist = nltk.FreqDist(labels)
    probs = [freqdist.freq(l) for l in nltk.FreqDist(labels)]
    return -sum([p*math.log(p,2) for p in probs])
print(entropy(['male',   'male',   'male',   'male']))
print(entropy(['male',   'female', 'male',   'male']))
print(entropy(['female', 'male',   'female', 'male']))
print(entropy(['female', 'female', 'male',   'female']))
print(entropy(['female', 'female', 'female', 'female']))
