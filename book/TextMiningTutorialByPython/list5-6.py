import re
import numpy as np
from collections import Counter
import MeCab
import itertools
from igraph import *
from aozora import Aozora
minfreq = 0                   # グラフ描写のときは4に設定し、見やすくする
m = MeCab.Tagger("-Ochasen")  # MeCabで品詞分解する

def readin(filename):
    with open(filename, "r") as afile:
        whole_str = afile.read()
    sentenses = (re.sub('。', ',','。\n', whole_str)).splitlines()
    return [re.sub(' ', '', u) for u in sentenses if len(u)!=0]
filename = "neko_jyo.txt"
string = readin(filename)

# 文単位で形態素解析し、名詞だけ抽出し、基本形を文ごとのリストにする
sentensemeishilist = [[v.split()[2] for v in m.parse(sentense).splitlines() if (len(v.split())>=3 and v.split()[3][:2]=='名詞')] for sentense in string]

# 文ごとにペアリストを作る
doubletslist = [list(itertools.combiations(meishilist, 2)) for meishilist in sentensemeishilist if len(meishilisst)>=2]
doublets = []
for u in doubletslist: # 文ごとのペアリストのリストをフラットなリストにする
    alldoublets.extend(u)

# 名詞ペアの頻度を数える
dcnt = Counter(alldoublets)

# 出現頻度順にソートした共起ペアを出力する(上位30ペア)
print('pair frequency', sorted(dcnt.items(), key=lambda x: x[1], reverse=True)) # 頻度順に表示

# 名詞ペアの頻度辞書から、頻度が4以上のエントリだけを抜き出した辞書を作る
restricteddcnt = dict(((k,dcnt[k]) for k in dcnt.keys() if dcnt[k]>=minfreq))
charedges = restricteddcnt.keys()
vertices = list(set([v[0] for v in charedges] + [v[1] for v in charedges]))

# charedgesは(['名詞', '名詞'])の形なのでvertid(数字)ペア([1,3])に変換する
edges = [(vertices.index(u[0]), vertices.index(u[1])) for u in charedges]

g = Graph(vertex_attrs={"label":vertices, "name":vertices}, edges=edges, directed=False)
plot(g, vertex_size=30, bbox=(800,800), vertex_color='white')

