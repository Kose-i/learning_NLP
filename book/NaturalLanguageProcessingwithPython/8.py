import nltk
from nltk.grammar import DependencyGrammar
from nltk import CFG
#groucho_grammar = nltk.parse_cfg("""
#groucho_grammar = DependencyGrammar.fromstring("""
groucho_grammar = nltk.CFG.fromstring("""
S -> NP VP
PP -> P NP
NP -> Det N | Det N PP | 'I'
VP -> V NP | VP PP
Det -> 'an' | 'my'
N -> 'elephant' | 'pajamas'
V -> 'shot'
P -> 'in'
""")
sent = ['I', 'shot', 'an', 'elephant', 'in', 'my', 'pajamas']
parser = nltk.ChartParser(groucho_grammar)
#trees = parser.nbest_parse(sent)
trees = next(parser.parse(sent))
for tree in trees:
    print(tree)

import nltk
#P314
