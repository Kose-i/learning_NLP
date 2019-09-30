#import nltk
#from nltk.grammar import DependencyGrammar
#from nltk import CFG
##groucho_grammar = nltk.parse_cfg("""
##groucho_grammar = DependencyGrammar.fromstring("""
#groucho_grammar = nltk.CFG.fromstring("""
#S -> NP VP
#PP -> P NP
#NP -> Det N | Det N PP | 'I'
#VP -> V NP | VP PP
#Det -> 'an' | 'my'
#N -> 'elephant' | 'pajamas'
#V -> 'shot'
#P -> 'in'
#""")
#sent = ['I', 'shot', 'an', 'elephant', 'in', 'my', 'pajamas']
#parser = nltk.ChartParser(groucho_grammar)
##trees = parser.nbest_parse(sent)
#trees = next(parser.parse(sent))
#for tree in trees:
#    print(tree)

#import nltk
#from nltk import CFG
#grammar1 = nltk.CFG.fromstring("""
#S -> NP VP
#VP -> V NP | V NP PP
#PP -> P NP
#V -> 'saw' | 'ate' | 'walked'
#NP -> 'John' | 'Mary' | 'Bob' | Det N | Det N PP
#Det -> 'a' | 'an' | 'the' | 'my'
#N -> 'man' | 'dog' | 'cat' | 'telescope' | 'park'
#P -> 'in' | 'on' | 'by' | 'with'
#""")
#sent = "Mary saw Bob".split()
#rd_parser = nltk.RecursiveDescentParser(grammar1)
#for tree in next(rd_parser.parse(sent)):
#    print(tree)
#grammar1 = nltk.data.load('file:mygrammar.cfg')
#sent = "Mary saw Bob".split()
#rd_parser = nltk.RecursiveDescentParser(grammar1)
#for tree in next(rd_parser.parse(sent)):
#    print(tree)
#grammar2 = nltk.CFG.fromstring("""
#S -> NP VP
#NP -> Det Nom | PropN
#Nom -> Adj Nom | N
#VP -> V Adj | V NP | V S | V NP PP
#PP -> P NP
#PropN -> 'Buster' | 'Chatterer' | 'Joe'
#Det -> 'the' | 'a'
#N -> 'bear' | 'squirrel' | 'tree' | 'fish' | 'log'
#Adj -> 'angry' | 'fringhtened' | 'little' | 'tall'
#V -> 'chased' | 'saw' | 'said' | 'thought' | 'was' | 'put'
#P -> 'on'
#""")

# P321 ~ 
