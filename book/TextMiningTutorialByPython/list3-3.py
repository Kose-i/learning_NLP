# -*- coding: utf-8 -*-
from aozora import Aozora
import re
import MeCab
import numpy as np
import matplotlib.pyplot as plt
aozora = Aozora("neko_jyo.txt")

# 文に分解する
string = '\n'.join(aozora.read())
string = re.sub(' ', '', string)
string = re.split('。(?!」)|\n', re.sub(' ','',string))
while '' in string:
    string.remove('') # 空行を除く
m = MeCab.Tagger("-Ochasen")

# 先頭20文について文単位で形態素解析し、名詞だけ抽出して、基本形を文ごとのリストにする
lengthlist = np.array([len(v) for v in string][3:23])
print('average', lengthlist.mean())
print('variance', lengthlist.var())
print('std-deviation', lengthlist.std())
for u in lengthlist:
    print(u)  # それぞれの文の長さを、出現順に表示
for u in sorted(lengthlist):
    print(u)  # それぞれの文の長さを、長さ順に表示
fig = plt.figure()
plt.title('文の長さ(文字数)')
plt.xlabel('長さ')
plt.ylabel('頻度')
plt.hist(lengthlist, color='blue', bins=40)  # binsでヒストグラムの横軸区分数を指定
plt.show()

# 箱ひげ図を作る
plt.boxplot(lengthlist)
plt.xticks([1],['吾輩'])
plt.title('箱ひげ図')
plt.grid()
plt.xlabel('文書')
plt.ylabel('文の長さの頻度')
plt.ylim([0,50])
plt.show()

