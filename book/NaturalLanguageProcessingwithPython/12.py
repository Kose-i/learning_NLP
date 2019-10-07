# -*- coding: utf-8 -*-

#import sys, codecs
#sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
#sys.stdin  = codecs.getreader('utf_8')(sys.stdin)
#f = codecs.open('sometext.txt', 'r', 'utf-8')
#print("%s で %s"%(u"パイソン", u"自然言語処理"))
#import sys
#print(sys.getdefaultencoding())
#reload(sys)
#sys.setdefaultencoding('utf-8')
#print("%s で %s"%(u"パイソン", u"自然言語処理"))
#import re, pprint
#def pp(obj):
#    pp = pprint.PrettyPrinter(indent=4, width=160)
#    str = pp.pformat(obj)
#    return re.sub(r"\\u([0-9a-f]{4})", lambda x: unichr(int("0x"+x.group(1), 16)))
#print(data)
#print(pp(data))

#import nltk
#from nltk.corpus.reader import *
#from nltk.corpus.reader.util import *
#from nltk.text import Text
#jp_sent_tokenizer = nltk.RegexpTokenizer(u'[^　「」！？。]*[！？。]')
#ginga = PlaintextCorpusReader("/path/to/dir/", r'gingatetsudono_yoru.txt', encoding='utf-8', para_block_reader=read_line_block, sent_tokenizer=jp_sent_tokenizer, word_okenizer=jp_chartype_tokenizer)
#print(ginga.raw())
#print('/'.join(ginga.words()[0:50]))
#ginga_t = Text(w.encode('utf-8') for w in ginga.words())
#ginga_t.concordance("川")
#from chasen import *
#jeita = ChasenCorpusReader('/path/to/jeita/corpus/', '.*chasen', encoding='utf-8')
#print('/'.join(jeita.words()[22100:22140]))
#print('\nEOS\n'.join(['\n'.join("%s/%s"%(w[0], w[1][2]) for w in sent) for sent in jeita.tagged_sents()[2170:2173]]))
#from knbc import *
#from nltk.corpus.util import LazyCorpusLoader
#root = nltk.data.find('corpora/knbc/corpus1')
#fileids = [f for f in find_corpus_fileids(FileSystemPathPointer(root), ".*") if re.search(r"\d\-\d\-[\d]+", f)]
#def _knbc_fileids_sort(x):
#    cells = x.split('-')
#    return (cells[0], int(cells[1]), int(cells[2]), int(cells[3]))
#knbc = LazyCorpusLoader('knbc/corpus1', KNBCorpusReader, sorted(fileids, key=_knbc_fileds_sort), encoding='euc-jp')
#print(knbc.fileids())
#print('\n'.join(''.join(sent) for sent in knbc.words()))
#print('\n\n'.join('%s'%tree for tree in knbc.parsed_sents()[0:2]))
#print('\n'.join(' '.join("%s%s"%(w[0],w[1][2]) for w in sent) for sent in knbc.tagged_words()[0:20]))
#genpaku = ChasenCorpusReader('/path/to/jeita/corpus/', 'g.*chasen', encoding='utf-8')
#print(len(genpaku.words()))
#print(sum(len(w) for w in genpaku.words()))
#import re
#genpaku_vocab = set(w for w in genpaku.words() if re.match(ur"^[ぁ-んーァ-ンー\u4e00-\u9FFF]+$", w))
#print(' '.join(sorted(genpaku_vocab)[:10]))
#genpaku_t = Text(genpaku.words())
#genpaku_wfd = FreqDist(genpaku_t)
#genpaku_wfd.tabulate(10)
#genpaku_tfd = FreqDist(t[2] for (w,t) in genpaku.tagged_words())
#genpaku_tfd.tabulate(10)
#genpaku_wfd.plot(100)
#print(' '.join(set(w for w,t in genpaku.tagged_words() if t[0]==u"コウショウ")))
#genpaku_t.collocations()
#genpaku_t.generate()
#genpaku_t.similar(u"ソフトウェア")
#class JapaneseWordNetCorpusReader(WordNetCorpusReader):
#    def __init__(self, root, filename):
#        WordNetCorpusReader.__init__(self, root)
#        import codecs
#        f=codecs.open(filename, encoding="utf-8")
#        self._jword2offset ={}
#        for line in f:
#            _cells = line.strip().split('\t')
#            _offset_pos = _cells[0]
#            _word = _cells[1]
#            if len(_cells)>2:
#                _tag = _cells[2]
#            _offset, _pos = _offset_pos.split('-')
#            self._jword2offset[_word] = {'offset': int(_offset), 'pos':_pos}
#    def synset(self, word):
#        if word in self._jword2offset:
#            return WordNetCorpusReader._synset_from_pos_and_offset(self, self._jword2offset[word]['pos'], self._jword2offset[word]['offset'])
#        else:
#            return None
#jwn = JapaneseWordNetCorpusReader(nltk.data.find('corpora/wordnet'), '/path/to/wnjpn-ok.tab')
#jsyn_whale  = jwn.synset(u"鯨")
#jsyn_apple  = jwn.synset(u"りんご")
#jsyn_orange = jwn.synset(u"ミカン")
#print(jsyn_apple.path_similarity(jsyn_orange))
#print(jsyn_whale.path_similarity(jsyn_orange))

#import nltk
#dict_entries = [
#  [u"かれ",   {'pos':'V-Y', 'lemma':u"枯れ"}],
#  [u"かれ",   {'pos':'V-Z', 'lemma':u"枯れ"}],
#  [u"かれ",   {'pos':'N',   'lemma':u"彼"}],
#  [u"の",     {'pos':'J-K', 'lemma':u"の"}],
#  [u"く",     {'pos':'N',   'lemma':u"区"}],
#  [u"くる",   {'pos':'V-S', 'lemma':u"来る"}],
#  [u"くる",   {'pos':'V-T', 'lemma':u"来る"}],
#  [u"くるま", {'pos':'N',   'lemma':u"車"}],
#  [u"ま",     {'pos':'N',   'lemma':u"間"}],
#  [u"まで",   {'pos':'J-F', 'lemma':u"まで"}],
#  [u"で",     {'pos':'J-K', 'lemma':u"で"}],
#  [u"でま",   {'pos':'N',   'lemma':u"デマ"}],
#  [u"まつ",   {'pos':'N',   'lemma':u"松"}],
#  [u"まつ",   {'pos':'V-S', 'lemma':u"待つ"}],
#  [u"まつ",   {'pos':'V-T', 'lemma':u"待つ"}],
#  [u"つ",     {'pos':'N',   'lemma':u"津"}]
#]
#def insert(trie, key, value):
#    if key:
#        first, rest = key[0], key[1:]
#        if first not in trie:
#            trie[first] = {}
#        else:
#            if not 'value' in trie:
#                trie['value'] = []
#            trie['value'].append(value)
#for entry in dict_entries:
#    entry[1]['length'] = len(entry[0])
#    insert(matrie, entry[0].encode('utf-8'), entry[1])
#def common_prefix_search(trie, key):
#    ret = []
#    if 'value' in trie:
#        ret += trie['value']
#    if key:
#        first, rest = key[0], key[1:]
#        if first in trie:
#            ret += common_prefix_search(trie[first], rest)
#        return ret
#def is_connectable(bnode, cnode):
#    ctable = set([
#      ('BOS', 'N'), ('BOS', 'V'), ('BOS', 'T'),
#      ('T', 'N'), ('N', 'J'), ('J', 'N'), ('J', 'V'),
#      ('V-T', 'N'), ('V-T', 'J-F'), ('V-Y', 'A'), ('V-S', 'EOS'), ('A', 'EOS')
#    ])
#    bpos = bnode['entry']['pos']
#    bpos_s = bpos.split('-')[0]
#    cpos = cnode['entry']['pos']
#    cpos_s = cpos.split('-')[0]
#    return (((bpos, cpos) in ctable) or ((bpos_s, cpos) in ctable) or ((bpos, cpos_s) in ctable) or ((bpos_s, cpos_s) in ctable))
#def analyze_simple(trie, sent, connect_func=lambda x,y:True):
#    bos_node = {'next':[], 'entry':_BOS_ENTRY}
#    end_node_list = nltk.defaultdict(list)
#    end_node_list[0].append(bos_node)
#    for i in range(0, len(sent)+1):
#        if i < len(sent):
#            cps_results = common_prefix_search(trie, sent[i:].encode('utf-8'))
#        else:
#            #EOS
#            cps_results = [_EOS_ENTRY]
#    for centry in cps_results:
#        cnode = {'next':[], 'entry': centry}
#        for bnode in end_node_list[i]:
#            if connect_func(bnode, cnode):
#                bnode['next'].append(cnode)
#                end_nodes = end_node_list[i+centry['length']]
#                if not cnode in end_nodes:
#                    end_nodes.append(cnode)
#    return enum_solutions(bos_node)
#def enum_solutions(node):
#    results = []
#    if node['entry']['lemma'] == u'EOS':
#        return [[u'EOS']]
#    for nnode in node['next']:
#        for solution in enum_solutions(nnode):
#            results.append([node['entry']['lemma']]+solution)
#    return results
#res = analyze_simple(matrie, u"かれのくるまでまつ", is_connectable)
#print('\n'.join(sent) for sent in res)
#def analyze(trie, sent, connect_func=lambda x,y: True, cost_func=lambda x,y: 0):
#    bos_node = {'begin':-1, 'next':[], 'entry':_BOS_ENTRY, 'cost': 0}
#    end_node_list = nltk.defaultdict(list)
#    end_node_list[0].append(bos_node)
#    for i in range(0, len(sent)+1):
#        if i < len(sent):
#            cps_results = common_prefix_search(trie, sent[i:].encode('utf-8'))
#        else:
#            #EOS
#            cps_results = [_EOS_ENTRY]
#        for centry in cps_results:
#            cnode = {'begin': i, 'next':[], 'entry':centry}
#            min_cost = -1
#            min_bnodes = []
#            for bnode in end_node_list[i]:
#                if connect_func(bnode, cnode):
#                    cost = bnode['cost']+cost_func(bnode, cnode)
#                    if min_cost < 0 or cost < min_cost:
#                        min_cost = cost
#                        min_bnodes = [bnode]
#                    elif cost == min_cost:
#                        min_bnodes.append(bnode)
#                if len(min_bnodes) > 0:
#                    for bnode in min_bnodes:
#                        cnode['cost'] = min_cost
#                        bnode['next'].append(cnode)
#                    end_nodes = end_node_list[i+centry['length']]
#                    if not cnode in end_nodes:
#                        end_nodes.append(cnode)
#    return enum_solutions(bos_node)
#dict_entries2 = [
#  [u"こ",       {'pos':'SF',  'lemma':u"個",   'cost':10}],
#  [u"この",     {'pos':'T',   'lemma':u"この", 'cost':10}],
#  [u"ひ",       {'pos':'N',   'lemma':u"日",   'cost':40}],
#  [u"ひと",     {'pos':'N',   'lemma':u"人",   'cost':40}],
#  [u"ひとこと", {'pos':'N',   'lemma':u"一言", 'cost':40}],
#  [u"と",       {'pos':'J',   'lemma':u"と",   'cost':10}],
#  [u"こと",     {'pos':'N',   'lemma':u"事",   'cost':10}],
#  [u"で",       {'pos':'V-Z', 'lemma':u"出",   'cost':40}],
#  [u"で",       {'pos':'V-Y', 'lemma':u"出",   'cost':40}],
#  [u"で",       {'pos':'J',   'lemma':u"で",   'cost':10}],
#  [u"げんき",   {'pos':'N',   'lemma':u"元気", 'cost':40}],
#  [u"に",       {'pos':'J',   'lemma':u"に",   'cost':10}],
#  [u"になっ",   {'pos':'V-Y', 'lemma':u"担っ", 'cost':40}],
#  [u"なっ",     {'pos':'V-Y', 'lemma':u"なっ", 'cost':40}],
#  [u"た",       {'pos':'A',   'lemma':u"た",   'cost':10}]
#]
#def cost_minimum(bnode, cnode):
#    ctable = {
#      ('BOS', 'T')  :10,
#      ('T', 'N')    :10,
#      ('N', 'J')    :10,
#      ('J', 'N')    :10,
#      ('N', 'N')    :10,
#      ('N', 'V-Z')  :40,
#      ('N', 'V-Y')  :40,
#      ('V-Z', 'N')  :40,
#      ('V-Y', 'N')  :40,
#      ('J', 'V-Z')  :10,
#      ('J', 'V-Y')  :10,
#      ('V-Y', 'A')  :10,
#      ('A', 'EOS')  :10,
#    }
#    pos2gram = (bnode['entry']['pos'], cnode['entry']['pos'])
#    return cnode['entry']['cost'] + (ctable[pos_2gram] if pos_2gram in ctable else 100)
#res = analyze(matrie2, u"このひとことでげんきになった", lambda x,y:True, lambda bnode,cnode:0)
#print('\n'.join('/'.join(sent) for sent in res))
#cost_morpheme_num = lambda bnode,cnode: 1
#jiritsugo = set(['N', 'V'])
#cost_bunsetsu_num = lambda bnode, cnode: 1 if cnode['entry']['pos'].split('-')[0] in jiritsugo else 0
#res = analyze(matrie2, u"このひとことでげんきになった", lambda x,y:True, cost_morpheme_num)
#print('\n'.join('/'.join(sent) for sent in res))
#res = analyze(matrie2, u"このひとことでげんきになった", lambda x,y:True, cost_morpheme_num)
#print('\n'.join('/'.join(sent) for sent in res))
#print(' '.join(reader.words()[20:80]))
#import MeCab
#mecab = MeCab.Tagger('-Ochasen')
#sent = u"かれのくるまでまつ".encode('utf-8')
#print(mecab.parse(sent))
#node = mecab.parseToNode(sent)
#node = node.next
#while node:
#    print(node.surface, node.feature)
#    node = node.next
#reader = PlaintextCorpusReader("/path/to/corpus/", r'gingatetsudono_yoru.txt', encoding='utf-8', para_block_reader=read_line_block, sent_tokenizer=jp_sent_tokenizer, word_tokenizer=jptokenizer.JPMeCabTokenizer())
#print(' '.join(reader.words()[20:80]))
#import cJuman
#cJuman.init(['-B', '-e2'])
#S = [u'30年も前に言語と画像を研究していた。'.encode('euc-jp')]
#print(cJuman.parse_opt(S, cJuman.SKIP_NO_RESULT).decode('euc-jp'))

#import nltk
#from nltk import CFG
#jpcfg1 = nltk.CFG.fromstring("""
#S    -> PP VP
#PP   -> NP P
#VP   -> PP VP
#VP   -> V TENS
#NP   -> NP 'の' NP
#NP   -> NP 'と' NP
#NP   -> N
#N    -> '先生' | '自転車' | '学校' | '僕'
#P    -> 'は' | 'が' | 'で' | 'に'
#V    -> '行k' | '殴r' | '見'
#TENS -> 'ru' | 'ita'
#""")
#sent = "先生 は 自転車 で 学校 に 行k ita".split(' ')
#parser = nltk.ChartParser(jpcfg1)
#for tree in next(parser.parse(sent)):
#    print(tree)
#sent = "先生 は 自転車 で 学校 に 行k ita".split(' ')
#parser = nltk.ChartParser(jpcfg1)
#for tree in next(parser.parse(sent)):
#    print(tree)
#genpaku = ChasenCorpusReader('/path/to/jeita/corpus/', 'g0014.chasen', encoding='utf-8')
#print('/'.join(genpaku.words()[80:120]))
#grammer = u"""
#JIRITSU: {<形容詞-自立>|<名詞.*>|<未知語>|<動詞-自立>|<記号-一般>|<副詞.*>}
#FUZOKU:  {<助動詞>|<助詞.*>|<動詞-接尾>|<動詞-非自立>|<名詞-非自立>}
#CHUNK:   {<JIRITSU>+<FUZOKU>*}
#"""
#cp = nltk.RegexpParser(grammer)
#print(cp.parse([(x, '-'.join(y[2].split('-')[0:2])) for x,y in genpaku.tagged_words()[80:120]]))
#import CaboCha, re
#cabocha = CaboCha.Parser('--charset=UTF8')
#sent = u"太郎はこの本を二郎を見た女性に渡した。".encode('utf-8')
#print(cabocha.perseToString(sent))
#tree = cabocha.parse(sent)
#print(tree.toString(CaboCha.FORMAT_LATTICE))
#def cabocha2depgraph(t):
#    dg = DependencyGraph()
#    i = 0
#    for line in t.splitlines():
#        if line.startswith("*"):
#            # start of bunsetsu
#            cells = line.strip().split(" ", 3)
#            m = re.match(r"([\-0-9]*)([ADIP])", cells[2])
#            node = dg.nodelist[i]
#            node.update(
#              {'address': i,
#               'rel': m.group(2), # dep_type
#               'word': [],
#               'tag': []
#              })
#            dep_parent = int(m.group(1))
#            while len(dg.nodelist) < i+1 or len(dg.nodelist) < dep_parent+1:
#                dg.nodelist.append({'word':[], 'deps':[], 'tag':[]})
#            if dep_parent == -1:
#                dg.root = node
#            else:
#                dg.nodelist[dep_parent]['deps'].append(i)
#            i += 1
#        elif not line.startswith("EOS"):
#            # normal morph
#            cells = line.strip().split("\t")
#            morph = (cells[0], tuple(cells[1].split(',')))
#            dg.nodelist[i-1]['word'].append(morph[0])
#            dg.nodelist[i-1]['tag'].append(morph[1])
#    return dg
#def reset_deps(dg):
#    for node in dg.nodelist:
#        node['deps'] = []
#    dg.root = dg.nodelist[-1]
#def set_head_form(dg):
#    for node in dg.nodelist:
#        tags = node['tag']
#        num_morphs = len(tags)
#        # extract bhead and bform
#        bhead = -1
#        bform = -1
#        for i in xrange(num_morphs - 1, -1, -1):
#            if tags[i][0] == u"記号":
#                continue
#            else:
#                if bform == -1:
#                    bform = i
#                if not (tags[i][0] == u"" or (tags[i][0] == u"" and tags[i][1] == u"") or tags[i][0] == ""):
#                    if bhead == -1:
#                        bhead = i
#        node['bhead'] = bhead
#        node['bform'] = bform
#NEXT_NODE = 1
#NEXT_VERB_NODE = 2
#NEXT_NOUN_NODE = 3
#def get_dep_type(node):
#    bform_tag = node['tag'][node['bform']]
#    if bform_tag[0] == u"助詞" and bform_tag[1] == u"格助詞":
#        return NEXT_VERB_NODE
#    elif bform_tag[0] == u"助動詞" and bform_tag[1] == u"夕":
#        return NEXT_NOUN_NODE
#    else:
#        return NEXT_NODE
#def analyze_dependency(dg):
#    num_nodes = len(dg.nodelist)
#    for i in xrange(num_nodes-1, 0, -1):
#        node = dg.nodelist[i]
#        if i == num_nodes-1:
#            #last node->to_node=0
#            to_node = 0
#        elif i == num_nodes-2:
#            #one from the last node -> to_node = num_nodes -1
#            to_node = num_nodes -1
#        else:
#            #other nodes
#            dep_type = get_dep_type(node)
#            if dep_type == NEXT_NODE:
#                to_node = i+1
#            elif dep_type == NEXT_VERB_NODE or dep_type == NEXT_NOUN_NODE:
#                for j in xrange(i+1, num_nodes):
#                    node_j = dg.nodelist[j]
#                    node_j_headtag = node_j['tag'][node_j['bhead']]
#                    if (node_j['closed'] == False and (dep_type == NEXT_VERB_NODE and node_j_headtag[0] == u"動詞") or 
#                                                      (dep_type == NEXT_NOUN_NODE and node_j_headtag[0] == u"名詞") and node_j_headtag[1] != u"形容動詞語幹"):
#                                                      to_node = j
#                                                      break
#                                                      node['head'] = to_node
#                                                      dg.nodelist[to_node]['deps'].append(i)
#                                                      for j in xrange(i+1, to_node):
#                                                          dg.nodelist[j]['closed'] = True
#
#cabocha_result = u"""*0 7D 0/1 0.000000
#太郎 名詞,固有名詞,人名,名,*,*,太郎,タロウ,タロー B-PERSON
#は 助詞,  係助詞,  *,   *, *,*,は,ハ,ワ        0
#* 1 2D 0/0 1.468291
#この 連体詞,   *,   *,   *, *,*,この,コノ,コノ 0
#* 2 4D 0/1 0.742535
#本 名詞,一般,*,*,*,*,本,ホン,ホン              0
#を 助詞,格助詞,一般,*,*,*,を,ヲ,ヲ             0
#* 3 4D 1/2 1.892480
#二 名詞,数,*,*,*,*,二,二,二                    0
#郎 名詞,一般,*,*,*,*,郎,ロウ,ロー              0
#を 助詞,格助詞,一般,*,*,*,を,ヲ,ヲ             0
#* 4 6D 0/1 0.702689
#見 動詞,自立,*,*,一段,連用形,見る,ミ,ミ        0
#た 助動詞,*,*,*,特殊・夕,基本形,た,タ,タ       0
#* 5 6D 0/1 1.193842
#きれい 名詞,形容動詞語幹,*,*,*,*,きれい,キレイ,キレイ   0
#な 助動詞,*,*,*,特殊・ダ,体言接続,だ,ナ,ナ     0
#* 6 7D 0/1 0.000000
#女性 名詞,一般,*,*,*,*,女性,ジョセイ,ジョセイ  0
#に 助詞,格助詞,一般,*,*,*,に,二,二             0
#* 7 -1D 0/1 0.000000
#渡し 動詞,自立,*,*,五段・サ行,連用形,渡す,ワタシ,ワタシ  0
#た 助動詞,*,*,*,特殊・タ,基本形,た,タ,タ       0
#。 記号,句点,*,*,*,*,。,。,。                  0
#EOS
#"""
#dg = cabocha2depgraph(cabocha_result)
#reset_deps(dg)
#set_head_form(dg)
#def _node_map(n):
#    node['word'] = '/'.join(node['word']).encode('utf-8')
#    return node
#analyze_handrules(dg)
#print(str(dg.tree()).decode('utf-8'))

#import nltk
#def extract_case_frame(dg):
#    res = []
#    for node in dg.nodelist:
#        if is_yogen(node):
#            for case_cand in [dg.nodelist[i] for i in node['deps']]:
#                if is_case(case_cand):
#                    res.append([yogen, case_cand])
#    return res
#def is_yogen(node):
#    bhead_tag = node['tag'][node['bhead']]
#    bform_tag = node['tag'][node['bform']]
#    if bhead_tag[0] ==u"動詞":
#        return True
#    elif bhead_tag[0] ==u"形容詞":
#        return True
#    elif bhead_tag[0] ==u"名詞" and bform_tag[0] ==u"助動詞":
#        return True
#    else:
#        return False
#def is_case(node):
#    bhead_tag = node['tag'][node['bhead']]
#    bform_tag = node['tag'][node['bform']]
#    bform_surface = bform_tag[-1]
#    if (bform_tag[0] == u"助詞" and bform_tag[1] == u"格助詞" and (bform_surface in set([u"ガ", u"ヲ", u"二", u"ト", u"デ", u"カラ", u"ヨリ", u"ヘ", u"マデ"]))):
#        return True
#    elif (bform_tag[0] == u"名詞" and bform_tag[0:2] == [u"名詞",u"接尾"]):
#        return True
#    else:
#        return False
