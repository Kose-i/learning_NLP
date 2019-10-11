import numpy as np
def gennext(words, dic): # N-gram辞書dicと直前の1語/2語から、次の語を選んで返す
    grams = len(words)   # 2-gramか3-gramかを、与えたwordが2語か3語かによって決める
    if grams == 2:
        matcheditems = np.array(list(filter(lambda x: x[0][0] == words[1]), dic.items())) # 2-gramの第2項が欲しい語words[1]であるものを集める
    else:
        matcheditems = np.array(list(filter((lambda x: x[0][0] == words[1]) and (lambda x: x[0][1] == words[2])), dic.items())) # 3-gramの第2・3項が欲しい語words[1]、word[2]であるものを集める
    if len(matcheditems) == 0: # ほしい語のパターンがN-gram辞書に無い場合は中止する
        print("No matched generator for", words[1])
        return ''
    probs = [row[1] for row in matcheditems] # N-gram辞書の出現回数部分を取り出す
    weightlist = rand(len(matcheditems)) * probs # 乱数rand(項数)を要素ごとに掛ける
    if grams==2:
        # 重み最大になる2-gramの2語目を取り出す
        u = matcheditems[np.argmax(weightlist)][0][1]
    else:
        # 重み最大になる3-gramの3語目を取り出す
        u = matcheditems[np.argmax(weightlist)][0][2]
    return u
if __name__=='__main__':
    #dict2, dict3 = ...
    # words = ['', '子規']     # 2-gram時の初期シーケンス
    words = ['', '子規', 'の'] # 3-gram時の初期シーケンス
    output = words[1:]         # 出力outputの先頭に初期シーケンスを埋め込む
    for i in range(50):        # 最大で50語まで生成(「。」などが来れば停止)
        if len(words) == 2:
            newword = gennext(words, dic2)  # 2-gram時の次の語の生成
        else:
            newword = gennext(words, dic3)   # 3-gram時の次の語の生成
        output.append(newword)               # 出力シーケンスoutputに次の語を加える
        if newword in ['', '。', '？', '！']:# 次の語が終端なら生成終了
            break
        words = output[-len(words):]         # 次のgentextの入力を準備する
    for u in output:
        print(u, end='')
    print()
