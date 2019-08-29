def q1():
    list_str = ["lion", "dog", "cat"]
    print(list_str + list_str)
    print(list_str*2)
    print(list_str[1])
    print(list_str[0:1])
    print(sorted(list_str))

from nltk.corpus import gutenberg
def q2():
    word_list = gutenberg.words('austen-persuasion.txt')
    print(len(word_list))
    print(len(set(word_list)))

import nltk
def q3():
    #print(nltk.corpus.brown.fileids())
    #print(nltk.corpus.webtext.fileids())
    brown_corpus_sample   = nltk.corpus.brown.words("ca02")
    webtext_corpus_sample = nltk.corpus.webtext.words('grail.txt')

def q4():
    print(nltk.corpus.state_union.fileids())
    #nltk.corpus.state_union.words('State')
    cfd = nltk.ConditionalFreqDist(
            (target, fileid[:4])
            for fileid in nltk.corpus.state_union.fileids()
            for w in nltk.corpus.state_union.words(fileid)
            for target in ['men', 'women', 'people']
            if w.lower().startswith(target)
            )
    cfd.plot()

from nltk.corpus import wordnet as wn
def q5():
    norn_list = ['cat.n.01', 'panda.n.01', 'student.n.01']
    for norn in norn_list:
        print(wn.synset(norn).member_meronyms())
        print(wn.synset(norn).part_meronyms())
        print(wn.synset(norn).substance_meronyms())
        print(wn.synset(norn).member_holonyms())
        print(wn.synset(norn).part_holonyms())
        print(wn.synset(norn).substance_holonyms())

from nltk.corpus import swadesh
def q6():
    ge2fr = swadesh.entries(['fr', 'en'])
    translate = dict(ge2fr)
    #print(translate['dog']) # ERROR
    print(translate.get('dog'))

#import urllib
def q7():
    #url = 'http://www.bartleby.com/141/strunk3.html'
    #with urllib.request.urlopen(url) as f:
    #    print(f.read().decode('utf-8'))
    emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
    emma.concordance('However')

def q8():
    names = nltk.corpus.names
    print(names.fileids())
    male_names   = names.words('male.txt')
    female_names = names.words('female.txt')
    cfd = nltk.ConditionalFreqDist(
            (fileid, name[0])
            for fileid in names.fileids()
            for name in names.words(fileid)
            )
    cfd.plot()

#from nltk.book import *
def q9(): #TODO <Not solved>
    target_file = [text1, text2]
    cfd = nltk.ConditionalFreqDist(
            (fileid, name[-1])
            for fileid in target_file
            for name in set(fileid)
            )
    cfd.plot()

def q10():
    fdist1 = FreqDist(text1)
    val = list(fdist1.values())
    val.sort(reverse=True)
    text1_len = len(text1)
    wordCount = 0
    sum_word = 0
    while True:
        sum_word += val[wordCount]
        wordCount += 1
        if sum_word*3 >= text1_len:
            break
    print(text1_len)
    print(wordCount)

from nltk.corpus import brown
def q11():
    list_houjo = ['can', 'must', 'may', 'shall', 'will', 'would', 'could', 'should', 'might']
    print(brown.categories())
    genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
    cfd = nltk.ConditionalFreqDist(
            (genre, word)
            for genre in brown.categories()
            for word in brown.words(categories=genre)
            )
    genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
    list_houjo = ['can', 'could', 'may', 'might', 'must', 'will']
    cfd.tabulate(conditions=genres, samples=list_houjo)

def q12():
    entries = nltk.corpus.cmudict.entries()
    pre_w = None
    for w, pron in entries:
        if w == pre_w:
            print(w, pron)
        pre_w = w

def q13():
    set_word = list(wn.all_synsets('n'))
    print(len(set_word))
    sum_count = 0
    for w in set_word:
        if not w.hypernyms():
            pass
        else:
            sum_count += 1
    print(sum_count)
    print(sum_count/len(set_word))

def q14():
    def supergloss(s):
        return_str = s
        for e in s:
            return_str += e.hypernyms()
        for e in s:
            return_str += e.hyponyms()
        return return_str
    print(supergloss(wn.synsets('motorcar')))

def q15():#TODO Too Long time
    word_brown = nltk.corpus.brown.words()
    for w in set(word_brown):
        if word_brown.count(w) >= 3:
            print(w)
    print(word_brown)

def q16():
    table_list = list()
    for genre in brown.categories():
        genre_list = list()
        genre_list.append(len(brown.words(categories=genre)))
        genre_list.append(len(set(brown.words(categories=genre))))
        genre_list.append(genre_list[0]/genre_list[1])
        table_list.append(genre_list)
    i = 0
    for genre in brown.categories():
        print(genre, end=' ')
        for e in table_list[i]:
            print(e, end=' ')
        i+=1
        print()
    #cfd = nltk.ConditionalFreqDist(
    #        (genre, word)
    #        for genre in brown.categories()
    #        for word in brown.words(categories=genre)
    #        )
    #tate = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
    #yoko = ['token', 'diff_items', 'kind']
    #cfd.tabulate(conditions=tate, samples=yoko)

from nltk.book import *
def q17():
    def del_stopword_print_fiftyword(text):
        stopword_list = ['the', 'to', 'also']
        return nltk.FreqDist([w for w in text if not w in stopword_list])
    target = del_stopword_print_fiftyword(text1)
    print(sorted(target, reverse=True)[0:50])

def q18():
    stopword_list = ['the', 'to', 'also']
    target = text1
    target = [w for w in target if not w in stopword_list]
    target_bigrams = nltk.bigrams(target)
    cfd = nltk.ConditionalFreqDist(target_bigrams)
    cfd.plot()

if __name__=='__main__':
    #q1()
    #q2()
    #q3()
    #q4()
    #q5()
    #q6()
    #q7()
    #q8()
    #q9()
    #q10()
    #q11()
    #q12()
    #q13()
    #q14()
    #q15()
    #q16()
    #q17()
    q18()
