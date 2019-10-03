#import nltk
#kim = {'CAT': 'NP', 'ORTH': 'Kim', 'REF': 'k'}
#chase = {'CAT': 'V', 'ORTH': 'chased', 'REL': 'chase'}
#chase['AGT'] = 'sbj'
#chase['PAT'] = 'obj'
#sent = "Kim chased Lee"
#tokens = sent.split()
#lee = {'CAT': 'NP', 'ORTH': 'Lee', 'REF': '1'}
#def lex2fs(word):
#    for fs in [kim, lee, chase]:
#        if fs['ORTH'] == word:
#            return fs
#subj, verb, obj = lex2fs(tokens[0]), lex2fs(tokens[1]), lex2fs(tokens[2])
#verb['AGT'] = subj['REF']              # agent of 'chase' is Kim
#verb['PAT'] = subj['REF']              # patient of 'chase' is Lee
#for k in ['ORTH', 'REL', 'AGT', 'PAT']:# check featstruct of 'chase'
#    print("%-5s => %s"%(k, verb[k]))
#surprise = {'CAT': 'V', 'ORTH': 'surprised', 'REL': 'surprise', 'SRC': 'sbj', 'EXP': 'obj'}
#nltk.data.show_cfg('grammars/book_grammars/feat0.fcfg')
#tokens = 'Kim likes children'.split()
#from nltk import load_parser
#cp = load_parser('grammars/book_grammars/feat0.fcfg', trace=2)
#trees = next(cp.parse(tokens))
#for tree in trees:
#    print(tree)

#import nltk
#fs1 = nltk.FeatStruct(TENSE='past', NUM='sg')
#print(fs1)
#fs1 = nltk.FeatStruct(PER=3, NUM='pl', GND='fem')
#print(fs1['GND'])
#fs1['CASE'] = 'acc'
#fs2 = nltk.FeatStruct(POS='N', AGR=fs1)
#print(fs2)
#print(fs2['AGR'])
#print(fs2['AGR']['PER'])
#print(nltk.FeatStruct("[POS='N', AGR=[PER=3, NUM='pl', GND='fem']]"))
#print(nltk.FeatStruct(name='Lee', telno='01 27 86 42 96', age=33))
#print(nltk.FeatStruct("""[NAME='Lee', ADDRESS=(1)[NUMBER=74, STREET='rue Pascal'], SPOUSE=[NAME='Kim', ADDRESS->(1)]]"""))
#print(nltk.FeatStruct("[A='a', B=(1)[C='c'], D->(1), E->(1)]"))
#fs1 = nltk.FeatStruct(NUMBER=74, STREET='rue Pascal')
#fs2 = nltk.FeatStruct(CITY='Paris')
#print(fs1.unify(fs2))
#print(fs2.unify(fs1))
#fs0 = nltk.FeatStruct(A='a')
#fs1 = nltk.FeatStruct(A='b')
#fs2 = fs0.unify(fs1)
#print(fs2)
#fs0 = nltk.FeatStruct("""[NAME='Lee', ADDRESS=[NUMBER=74, STREET='rue Pascal'], SPOUSE=[NAME='Kim', ADDRESS=[NUMBER=74, STREET='rue Pascal']]]""")
#print(fs0)
#fs1 = nltk.FeatStruct("[SPOUSE=[ADDRESS=[CITY=Paris]]]")
#print(fs1.unify(fs0))
#fs2 = nltk.FeatStruct("""[NAME='Lee', ADDRESS=(1)[NUMBER=74, STREET='rue Pascal'], SPOUSE=[NAME='Kim', ADDRESS->(1)]]""")
#print(fs1.unify(fs2))
#fs1 = nltk.FeatStruct("[ADDRESS1=[NUMBER=74, STREET='rue Pascal']]")
#fs2 = nltk.FeatStruct("[ADDRESS1=?x, ADDRESS2=?x]")
#print(fs2)
#print(fs2.unify(fs1))

import nltk
