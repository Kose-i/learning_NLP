# 前準備
import nltk
from nltk.corpus  import wordnet
from nltk.corpus.reader import WordNetCorpusReader, WordNetICCorpusReader
wn = WordNetCorpusReader(nltk.data.find('corpora/wordnet'), None)
S = wn.synset
L = wn.lemma

# synsetの基本メソッド
s = S('go.v.21')      # 単語goの動詞の21番のsynsetを読み出す
# synsetの名前がmove.v.15 pos (品詞名) がv辞書ファイルがverb.competition
print(s.name(), s.pos(), s.lexname())
print(s.lemma_names())# synset goの語彙は['move','go']
print(s.definition()) # goの定義は"have a turn; make one's move in a game"
print(s.examples())   # goの例文は['Can I go now?']

# リンクを辿ってみる
s = S('dog.n.01')
print(s.hypernyms()) # dogの上位概念は[Synset('canine.n.02'), Synset('domestic_animal.n.01')]
print(L('zap.v.03.nuke').derivationally_related_forms()) # [Lemma('atomic_warhead.n.01.nuke')]
print(L('zap.v.03.atomize').derivationally_related_forms()) # [Lemma('atomization.n.02.atomization')]

print(s.member_holonyms()) # [Synset('canis.n.01'), Synset('pack.n.06')]
print(s.part_meronyms())   # [Synset('flag.n.07')]
print(S('Austen.n.1').instance_hyponyms()) # Austeinが例であるような上位概念[Synset('writer.n.01')]
print(S('composer.n.1').instance_hyponyms()) # 作家の例(作曲家が多数表示される)

print(S('faculty.n.2').member_meronyms()) # 一部分(メンバー)[Synset('professor.n.01')]
print(S('copilot.n.1').member_holonyms()) # これが含まれる大きな集合[Synset('crew.n.01')]
print(S('table.n.2').part_meronyms())     # 一部分[Synset('leg.n.03'), Synset('tabletop.n.01'), Synset('tableware.n.01')]
print(S('course.n.7').part_holonyms())    # 含まれる集合[Synset('meal.n.01')]
print(S('water.n.1').substance_meronyms())# 一部分(材料)[Synset('hydrogen.n.01'), Synset('oxygen.n.01')]
print(S('gin.n.1').substance_holonyms())  # [Synset('gin_and_it.n.01'), Synset('gin_and_tonic.n.01')]
print(S('snore.v.1').entailments())       # 論理的な結合[Synset('sleep.v.01')]
print(S('heavy.a.1').similar_tos())
# [Synset('dense.s.03'), Synset('doughy.s.01'), Synset('heavier-than-air.s.01'), Synset('hefty.s.02'), Synset('massive.s.04'), Synset('non-buoyant.s.01'), Synset('ponderous.s.02')]
print(S('light.a.1').attributes())        # 属性[Synset('weight.n.01')]
print(S('heavy.a.1').attributes())        # 属性[Synset('weight.n.01')]

print(S('person.n.01').root_hypernyms())  # 意味トリーのルート[Synset('entity.n.01')]

# 二者の関係(二者の間ではじめて共通する概念)
print(S('person.n.01').lowest_common_hypernyms(S('dog.n.01'))) # はじめて共通する概念
# 結果はSynset('organism.n.01')
print(S('woman.n.01').lowest_common_hypernyms(S('girlfriend.n.02'))) # 結果は[Synset('woman.n.01')]
# 結果はSynset('woman.n.01')
