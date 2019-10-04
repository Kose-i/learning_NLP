#import nltk
#nltk.data.show_cfg('grammars/book_grammars/sq10.fcfg')
#from nltk import load_parser
#cp = load_parser('grammars/book_grammars/sq10.fcfg')
#query = 'What cities are located in China'
#trees = next(cp.parse(query.split()))
#answer = trees[0].label('SEM')
#q = ' '.join(answer)
#print(q)
#from nltk.sem import chat80
#rows = chat80.sql_query('corpora/city_database/city.db', q)
#for r in rows:
#    print(r[0],)

#import nltk
#from nltk.sem.logic import LogicParser
#nltk.boolean_ops()
#lp = nltk.sem.logic.LogicParser()
#lp.parse('-(P & Q)')
#lp.parse('P & Q')
#lp.parse('P | (R -> Q)')
#lp.parse('P <-> -- P')
#lp = nltk.sem.logic.LogicParser()
#SnF = lp.parse('SnF')
#NotFnS = lp.parse('-FnS')
#R = lp.parse('SnF -> -FnS')
#prover = nltk.Prover9()
#print(prover.prove(NotFnS, [SnF, R]))
#val = nltk.Valuation([('P', True), ('Q', True), ('R', False)])
#print(val['P'])
#dom = set([])
#g = nltk.Assignment(dom)
#m = nltk.Model(dom, val)
#print(m.evaluate('(P & Q)', g))
#print(m.evaluate('-(P & Q)', g))
#print(m.evaluate('(P | R)', g))

#import nltk
#tlp = nltk.sem.logic.LogicParser(type_check=True)
#parsed = tlp.parse('walk(angus)')
#print(parsed.argument)
#print(parsed.argument.type)
#print(parsed.function)
#print(parsed.function.type)
#sig = {'walk':'<e, t>'}
#parsed = tlp.parse('walk(angus)', sig)
#print(parsed.function.type)
#lp = nltk.sem.logic.LogicParser()
#print(lp.parse('dog(cyril)').free())
#print(lp.parse('dog(x)').free())
#print(lp.parse('own(angus, cyril)').free())
#print(lp.parse('exists x.dog(x)').free())
#print(lp.parse('((some x. walk(x)) -> sing(x))').free())
#NotFnS = lp.parse('-north_of(f, s)')
#SnF = lp.parse('north_of(s, f)')
#R = lp.parse('all x. all y. (north_of(x,y) -> -north_of(y, x))')
#prover = nltk.Prover9()
#print(prover.prove(NotFnS, [SnF, R]))
#FnS = lp.parse('north_of(f, s)')
#print(prover.prove(FnS, [SnF, R]))
#dom = set(['b', 'o', 'c'])
#v = """
#bertie => b
#olive => o
#cyril => c
#boy => {b}
#girl => {o}
#dog => {c}
#walk => {o, c}
#see => {(b,o), (c,b), (o,c)}
#"""
#import nltk.sem.util
#val = nltk.sem.util.parse_valuation(v)
#print(val)
#print(('o', 'c') in val['see'])
#print(('b',) in val['boy'])
#g = nltk.Assignment(dom, [('x', 'o'), ('y', 'c')])
#print(g)
#m = nltk.Model(dom, val)
#print(m.evaluate('see(olive, y)', g))
#print(g['y'])
#print(m.evaluate('see(y, x)', g))
#g.purge()
#print(g)
#print(m.evaluate('see(olive, y)', g))
#print(m.evaluate('see(bertie, olive) & boy(bertie) & -walk(bertie)', g))
#print(m.evaluate('exists x.(girl(x) & walk(x))', g))
#print(m.evaluate('girl(x) & walk(x)', g.add('x', 'o')))
#fmla1 = lp.parse('girl(x) | boy(x)')
#print(m.satisfiers(fmla1, 'x', g))
#fmla2 = lp.parse('girl(x) -> walk(x)')
#print(m.satisfiers(fmla2, 'x', g))
#fmla3 = lp.parse('walk(x) -> girl(x)')
#print(m.satisfiers(fmla3, 'x', g))
#print(m.evaluate('all x.(girl(x) -> walk(x))', g))
#v2 = """
#bruce => b
#cyril => c
#elspeth => e
#julia => j
#matthew => m
#person => {b,e,j,m}
#admire => {(j,b), (b,b), (m,e), (e,m), (c,a)}
#"""
#val2 = nltk.parse_valuation(v2)
#dom2 = val2.domain
#m2 = nltk.Model(dom2, val2)
#g2 = nltk.Assignment(dom2)
#fmla4 = lp.parse('(person(x) -> exists y.(person(y) & admire(x,y)))')
#print(m2.satiffiers(fmla4, 'x', g2))
#fmla5 = lp.parse('(person(y) & all x.(person(x) -> admire(x,y)))')
#print(m2.satisfiers(fmla5, 'y', g2))
#fmla6 = lp.parse('(person(y) & all x.((x = bruce | x = julia) -> admire(x,y)))')
#print(m2.satiffiers(fmla6, 'y', g2))
#a3 = lp.parse('exists x.(man(x) & walks(x))')
#c1 = lp.parse('mortal(socrates)')
#c2 = lp.parse('-mortal(socrates)')
#mb = nltk.Mace(5)
#print(mb.build_model(None, [a3, c1]))
#print(mb.build_model(None, [a3, c2]))
#print(mb.build_model(None, [c1, c1]))
#a4 = lp.parse('exists y. (woman(y) & all x. (man(x) -> love(x,y)))')
#a5 = lp.parse('man(adam)')
#a6 = lp.parse('woman(eve)')
#g = lp.parse('love(adam, eve)')
#mc = nltk.MaceCommand(g, assumptions=[a4, a5, a6])
#print(mc.build_model())
#print(mc.valuation)
#a7 = lp.parse('all x. (man(x) -> -woman(x))')
#g = lp.parse('love(adam, eve)')
#mc = nltk.MaceCommand(g, assumptions=[a4,a5,a6,a7])
#print(mc.build_model())
#print(mc.valuation)

#import nltk
#lp = nltk.sem.logic.LogicParser()
#e = lp.parse(r'\x.(walk(x) & chew_gum(x))')
#print(e)
#print(e.free())
#print(lp.parse(r'\x.(walk(x) & chew_gum(y))'))
#e = lp.parse(r'\x.(walk(x) & chew_gum(x))(gerald)')
#print(e)
#print(e.simplify())
#print(lp.parse(r'\x.\y.(dog(x) & own(y,x))(cyril)').simplify())
#print(lp.parse(r'\x y.(dog(x) & own(y,x))(cyril, angus)').simplify())
#e1 = lp.parse('exists x.P(x)')
#print(e1)
#e2 = e1.alpha_convert(nltk.sem.Variable('z'))
#print(e2)
#print(e1==e2)
#e3 = lp.parse('\P.exists x.P(x)(\y.see(y,x))')
#print(e3)
#print(e3.simplify())
#lp = nltk.sem.logic.LogicParser()
#tvp = lp.parse(r'\X x.X(\y.chase(x,y))')
#np = lp.parse(r'(\P.exists x.(dog(x) & P(x)))')
#vp = nltk.sem.ApplicationExpression(tvp, np)
#print(vp)
#print(vp.simplify())
#from nltk import load_parser
#parser = load_parser('grammars/book_grammars/simple-sem.fcfg', trace=0)
#sentence = 'Angus gives a bone to every dog'
#tokens = sentence.split()
#trees = next(parser.parse(tokens))
#for tree in trees:
#    print(tree.label()['SEM'])
#v = """
#bertie => b
#olive => o
#cyril => c
#boy => {b}
#girl => {o}
#dog => {c}
#walk => {o, c}
#see => {(b,o), (c,b), (o,c)}
#"""
#val = nltk.parse_valuation(v)
#g = nltk.Assignment(val.domain)
#m = nltk.Model(val.domain, val)
#sent = 'Cyril sees every boy'
#grammar_file = 'grammars/book_grammars/simple-sem.fcfg'
#results = nltk.batch_evaluate([sent], grammar_file, m, g)[0]
#for (syntree, semrep, value) in results:
#    print(semrep)
#    print(value)
#from nltk.sem import cooper_storage as cs
#sentence = 'every girl chases a dog'
#trees = cs.parse_with_bindops(sentence, grammar='grammars/book_grammars/storage.fcfg')
#semrep = trees[0].label('SEM')
#print(cs_semrep.core)
#for bo in cs_semrep.store:
#    print(bo)
#cs_semrep.s_retrieve(trace=True)
#for reading in cs_semrep.readings:
#    print(reading)

#import nltk
#dp = nltk.DrtParser()
#drs1 = dp.parse('([x,y], [angus(x), dog(y), own(x,y)])')
#print(drs1)
#drs1.draw()
#print(drs1.fol())
#drs2 = dp.parse('([x], [walk(x)]) + ([y], [run(y)])')
#print(drs2)
#print(drs2.simplify())
#drs3 = dp.parse('([], [(([x],[dog(x)]) -> ([y], [ankle(y), bite(x,y)]))])')
#print(drs3.fol())
#drs4 = dp.parse('([x,y], [angus(x), dog(y)  , own(x,y) ])')
#drs5 = dp.parse('([u,z], [PRO(u)  , irene(z), bite(u,z)])')
#drs6 = drs4 + drs5
#print(drs6.simplify())
#print(drs6.simplify().resolve_anaphora())
#from nltk import load_parser
#parser = load_parser('grammars/book_grammars/drt.fcfg', logic_parser=nltk.DrtParser())
#trees = next(parser.parse('Angus owns a dog'.split()))
#print(trees[0].label()['SEM'].simplify())
#dt = nltk.DiscourseTester(['A student dances', 'Every student is a person'])
#dt.readings()
#dt.add_sentence('No person dances', consistchk=True)
#dt.retract_sentence('No person dances', verbose=True)
#dt.add_sentence('A person dances', informchk=True)
#from nltk.tag import RegexpTagger
#tagger = RegexpTagger(
#            [('^(chases|runs)$', 'VB'),
#             ('^(a)$', 'ex_quant'),
#             ('^(every)$', 'univ_quant'),
#             ('^(dog|boy)$', 'NN'),
#             ('^(He)$', 'PRP')
#            ]
#        )
#rc = nltk.DrtGlueReadingCommand(depparser=nltk.MaltParser(tagger=tagger))
#dt = nltk.DiscourseTester(['Every dog chases a boy', 'He runs'], rc)
#dt.readings()
#dt.readings(show_thread_readings=True)
#dt.readings(show_thread_readings=True, filter=True)
