#import nltk
#phonetic = nltk.corpus.timit.phones('dr1-fvmh0/sa1')
#print(phonetic)
#print(nltk.corpus.timit.word_times('dr1-fvmh0/sa1'))
#timitdict = nltk.corpus.timit.transcription_dict()
#print(timitdict['greasy'] + timitdict['wash'] + timitdict['water'])
#print(phonetic[17:30])
#print(nltk.corpus.timit.spkrinfo('dr1-fvmh0'))

#import nltk
#s1  = "00000010000000001000000"
#s2  = "00000001000000010000000"
#s3  = "00010000000000000001000"
#print(nltk.windowdiff(s1,s1,3))
#print(nltk.windowdiff(s1,s2,3))
#print(nltk.windowdiff(s2,s3,3))

#import nltk, re
#import requests
#from bs4 import BeautifulSoup
#legal_pos = set(['n', 'v.t.', 'v.i.', 'adj', 'det'])
#pattern = re.compile(r"'font-size:11.0pt'>([a-z.]+)<")
#document = open("dict.html").read()
#used_pos = set(re.findall(pattern, document))
#illegal_pos = used_pos.difference(legal_pos)
#print(list(illegal_pos))
#def lexical_data(html_file):
#    SEP = '_ENTRY'
#    html = open(html_file).read()
#    html = re.sub(r'<p', SEP + '<p', html)
#    #text = nltk.clean_html(html)
#    text = BeautifulSoup(html).get_text()
#    text = ' '.join(text.split())
#    for entry in text.split(SEP):
#        if entry.count(' ')>2:
#            yield entry.split(' ',3)
#import csv
#writer = csv.writer(open("dict1.csv", "wb"))
#writer.writerows(lexical_data("dict.html"))
#import csv
#lexicon = csv.reader(open('dict.csv'))
#pairs = [(lexeme, defn) for (lexeme, _, _, defn) in lexicon]
#lexemes, defns = zip(*pairs)
#defn_words = set(w for defn in defns for w in defn.split())
#print(sorted(defn_words.difference(lexemes)))
#idx = nltk.Index((defn_word, lexeme) for (lexeme, defn) in pairs for defn_word in nltk.word_tokenize(defn) if len(defn_word)>3)
#idx_file = open("dict.idx", "w")
#for word in sorted(idx):
#    idx_words = ', '.join(idx[word])
#    idx_line = "%s: %s\n"%(word, idx_words)
#    idx_file.write(idx_line)
#idx_file.close()
#mappings = [('ph', 'f'), ('ght', 't'), ('^kn', 'n'), ('qu', 'kw'), ('[aeiou]+', 'a'), (r'(.)\1', r'\1')]
#def signature(word):
#    for patt, repl in mappings:
#        word = re.sub(patt, repl, word)
#        pieces = re.findall('[^aeiou]+', word)
#        return ''.join(char for piece in pieces for char in sorted(piece))[:8]
#print(signature('illefent'))
#print(signature('ebsekwieous'))
#print(signature('nuculerr'))
#signatures = nltk.Index((signature(w), w) for w in nltk.corpus.words.words())
#print(signatures[signature('nuculerr')])
#def rank(word, wordlist):
#    ranked = sorted((nltk.edit_dist(word, w), w) for w in wordlist)
#    return [word for (_, word) in ranked]
#def fuzzy_spell(word):
#    sig = signature(word)
#    if sig in signatures:
#        return rank(word, signatures[sig])
#    else:
#        return []
#print(fuzzy_spell('illefent'))
#print(fuzzy_spell('ebsekwieous'))
#print(fuzzy_spell('nucular'))

#import nltk
#merchant_file = nltk.data.find('corpora/shakespeare/merchant.xml')
#raw = open(merchant_file).read()
#print(raw[0:168])
#print(raw[1850:2075])
#from xml.etree.ElementTree import ElementTree
#merchant = ElementTree().parse(merchant_file)
#print(merchant)
#print(merchant[0])
#print(merchant[0].text)
#print(merchant.getchildren())
#print(merchant[-2][0].text)
#print(merchant[-2][0])
#print(merchant[-2][1][0].text)
#print(merchant[-2][1][54])
#print(merchant[-2][1][54][0])
#print(merchant[-2][1][54][0].text)
#print(merchant[-2][1][54][1])
#print(merchant[-2][1][54][1].text)
#for i, act in enumerate(merchant.findall('ACT')):
#    for j, scene in enumerate(act.findall('SCENE')):
#        for k, speech in enumerate(scene.findall('SPEECH')):
#            for line in speech.findall('LINE'):
#                if 'music' in str(line.text):
#                    print("Act %d Scene %d Speech %d: %s"%(i+1, j+1, k+1, line.text))
#speaker_seq = [s.text for s in merchant.findall('ACT/SCENE/SPEECH/SPEAKER')]
#speaker_frep = nltk.FreqDist(speaker_seq)
#top5 = list(speaker_frep.keys())[:5]
#print(top5)
#mapping = nltk.defaultdict(lambda: 'OTH')
#for s in top5:
#    mapping[s] = s[:4]
#speaker_seq2 = [mapping[s] for s in speaker_seq]
#cfd = nltk.ConditionalFreqDist(nltk.bigrams(speaker_seq2))
#cfd.tabulate()
#from nltk.corpus import toolbox
#lexicon = toolbox.xml('rotokas.dic')
#print(lexicon[3][0])
#print(lexicon[3][0].tag)
#print(lexicon[3][0].text)
#print([lexeme.text.lower() for lexeme in lexicon.findall('record/lx')])
#import sys
#from xml.etree.ElementTree import ElementTree
#tree = ElementTree(lexicon[3])
#print(tree)
#html = "<table>\n"
#for entry in lexicon[70][80]:
#    lx = entry.findtext('lx')
#    ps = entry.findtext('ps')
#    ge = entry.findtext('ge')
#    html += "  <tr><td>%s</td><td>%s</td><td>%s</td></tr>\n"%(lx, ps, ge)
#html += "</table>"
#print(html)

#import nltk, re
#from nltk.corpus import toolbox
#lexicon = toolbox.xml('rotokas.dic')
#print(sum(len(entry) for entry in lexicon) / len(lexicon))
#from xml.etree.ElementTree import SubElement
#def cv(s):
#    s = s.lower()
#    s = re.sub(r'[^a-z]',  r'_', s)
#    s = re.sub(r'[aeiou]', r'V', s)
#    s = re.sub(r'[^V_]',   r'C', s)
#    return (s)
#def add_cv_field(entry):
#    for field in entry:
#        if field.tag == 'lx':
#            cv_field = SubElement(entry, 'cv')
#            cv_field.text = cv(field.text)
#lexicon = toolbox.xml('rotokas.dic')
#add_cv_field(lexicon[53])
#print(nltk.toolbox.to_sfm_string(lexicon[53]))
#fd = nltk.FreqDist(':'.join(field.tag for field in entry) for entry in lexicon)
#print(fd.items())
#from nltk import CFG
#grammar = nltk.CFG.fromstring("""
#S -> Head PS Glosses Comment Data Sem_Field Examples
#Head -> Lexeme Root
#Lexeme -> "lx"
#Root -> "rt" |
#PS -> "ps"
#Glosses -> Gloss Glosses |
#Gloss -> "ge" | "tkp" | "eng"
#Date -> "dt"
#Examples -> Example Ex_Pidgin Ex_English Examples |
#Example -> "ex"
#Ex_Pidgin -> "xp"
#Ex_English -> "xe"
#Comment -> "cmt" | "nt" |
#""")
#def validate_lexicon(grammar, lexicon, ignored_tags):
#    rd_parser = nltk.RecursiveDescentParser(grammar)
#    for entry in lexicon:
#        marker_list = [field.tag for field in entry if field.tag not in ignored_tags]
#        if next(rd_parser.parse(marker_list)):
#            print("+", ':'.join(marker_list))
#        else:
#            print("-", ':'.join(marker_list))
#lexicon = toolbox.xml('rotokas.dic')[10:20]
#ignored_tags = ['arg', 'dcsv', 'pt', 'vx']
#validate_lexicon(grammar, lexicon, ignored_tags)
#from nltk_contrib import toolbox
#grammar = r"""
#lexfunc: {<lf>(<lv><ln|le>*)*}
#example: {<rf|xv><xn|xe>*}
#sense: {<sn><ps><pn|gv|dv|gn|gp|dn|rn|ge|de|re>*<example>*<lexfunc>*}
#record: {<lx><hm><sense>+<dt>}
#"""
#from xml.etree.ElementTree import ElementTree
#db = toolbox.ToolboxData()
#db.open(nltk.data.find('corpora/toolbox/iu_mien_samp.db'))
#lexicon = db.parse(grammar, encoding='utf8')
#toolbox.data.indent(lexicon)
#tree = ElementTree(lexicon)
#output = open("iu_mien_samp.xml", "w")
#tree.write(output, encoding='utf8')
#output.close()
