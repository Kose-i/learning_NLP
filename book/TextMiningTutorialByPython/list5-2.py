from collections import Counter
import numpy as np
from numpy.random import *
import nltk
from nltk.corpus.reader.chasen import *
# JEITA コーパスデータの読み込み
jeita = ChasenCorpusReader('./corpus/', 'a1000.chasen', encoding='utf-8')
delimiter=['「','」','・・・',' '] # N-gramデータで対象外にする文字のリスト
string = jeita.words()
doublets = list(zip(string[:-1], string[1:]))
doublets = filter((lambda x: not((x[0] in delimiter) or (x[1] in delimiter))), doublets)

triplets = list(zip(string[:-2], string[1:-1], string[2:]))
triplets = filter((lambda x: not((x[0] in delimiter) or (x[1] in delimiter) or (x[2] in delimiter))), triplets)

dict2 = Counter(doublets)
dict3 = Counter(triplets)
for k,v in dict2.items():
    print(k,v)
for k,v in dict3.items():
    print(k,v)
