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
#rd_parser = nltk.RecursiveDescentParser(grammar1)
#sent = "Mary saw a dog".split()
#for t in rd_parser.parse(sent):
#    print(t)
#sr_parse = nltk.ShiftReduceParser(grammar1)
#sent = "Mary saw a dog".split()
#print(sr_parse.parse(sent))
#text = ['I', 'shot', 'an', 'elephant', 'in', 'my', 'pajamas']
#def init_wfst(tokens, grammar):
#    numtokens = len(tokens)
#    wfst = [[None for i in range(numtokens+1)] for j in range(numtokens+1)]
#    for i in range(numtokens):
#        productions = grammar.productions(rhs=tokens[i])
#        wfst[i][i+1] = productions[0].lhs()
#    return wfst
#def complete_wfst(wfst, tokens, grammar, trace=False):
#    index = dict((p.rhs(), p.lhs()) for p in grammar.productions())
#    numtokens = len(tokens)
#    for span in range(2,numtokens+1):
#        for start in range(numtokens+1-span):
#            end = start + span
#            for mid in range(start+1,end):
#                nt1, nt2 = wfst[start][mid], wfst[mid][end]
#                if nt1 and nt2 and (nt1, nt2) in index:
#                    wfst[start][end] = index[(nt1, nt2)]
#                    if trace:
#                        print("[%s] %3s [%s] %3s [%s] ==> [%s] %3s [%s]"%(start, nt1, mid, nt2, end, start, index[(nt1,nt2)], end) ,end=' ')
#    return wfst
#def display(wfst, tokens):
#    print("\nWFST"+' '.join([("%-4d"%i) for i in range(1,len(wfst))]))
#    for i in range(len(wfst)-1):
#        print("%d"%i,end=' ')
#        for j in range(1,len(wfst)):
#            print("%-4s"%(wfst[i][j] or '.'),end=' ')
#        print()
#tokens = "I shot an elephant in my pajamas".split()
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
#wfst0 = init_wfst(tokens, groucho_grammar)
#display(wfst0, tokens)
#wfst1 = complete_wfst(wfst0, tokens, groucho_grammar)
#display(wfst1, tokens)
#wfst1 = complete_wfst(wfst0, tokens, groucho_grammar, trace=True)

#import nltk
#from nltk import DependencyGrammar
#from nltk.parse import DependencyGraph
#groucho_dep_grammar = nltk.parse_dependency_grammar("""
#'shot' -> 'I' | 'elephant' | 'in'
#'elephant' -> 'an' | 'in'
#'in' -> 'pajamas'
#'pajamas' -> 'my'
#"""
#)
#print(groucho_dep_grammar)
#pdp = nltk.ProjectiveDependencyParser(groucho_dep_grammar)
#sent = 'I shot an elephant in my pajamas'.split()
#trees = pdp.parse(sent)
#for tree in trees:
#    print(tree)

import nltk
from nltk.corpus import treebank
t = treebank.parsed_sents('wsj_0001.mrg')[0]
print(t)
def filter(tree):
    child_nodes = [child.label() for child in tree if isinstance(child, nltk.Tree)]
    return (tree.label() == 'VP') and ('S' in child_nodes)
from nltk.corpus import treebank
print([subtree for tree in treebank.parsed_sents() for subtree in tree.subtrees(filter)])
entries = nltk.corpus.ppattach.attachments('training')
table = nltk.defaultdict(lambda: nltk.defaultdict(set))
for entry in entries:
    key = entry.noun1 + '-' + entry.prep + '-' + entry.noun2
    table[key][entry.attachment].add(entry.verb)
for key in sorted(table):
    if len(table[key]) > 1:
        print(key, 'N:', sorted(table[key]['N']), 'V:', sorted(table[key]['V']))
from nltk import CFG
grammar = nltk.CFG.fromstring("""
S -> NP V NP
NP -> NP Sbar
Sbar -> NP V
NP -> 'fish'
V -> 'fish'
""")
tokens = ["fish"]*5
cp = nltk.ChartParser(grammar)
for tree in next(cp.parse(tokens)):
    print(tree)
def give(t):
    return t.label() == 'VP' and len(t) > 2 and t[1].label() == 'NP' and (t[2].label() == 'PP-DTV' or t[2].label() == 'NP') \
           and ('give' in t[0].leaves() or 'gave' in t[0].leaves())
def sent(t):
    return ' '.join(token for token in t.leaves() if token[0] not in '*-0')
#P339
def print_node(t, width):
    output = "%s %s: %s"

