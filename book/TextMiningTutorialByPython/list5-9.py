from aozora import Aozora
import MeCab
import nltk

aozora = Aozora("neko_jyo.txt")
m = MeCab.Tagger("-Owakati -b65535")
string = m.parse('\n'.join(aozora.read()))
text = nltk.Text(nltk.word_tokenize(string)) # NLTKでトークン化し、Textのフォーマットに変換する
word = '吾輩'
c = nltk.text.ConcordanceIndex(text) # ConcordanceIndexクラスのインスタンス生成、入力textを指定
c.print_concordance(word, width=40)  # 検索語wordでKWIC形式を表示
print(c.offsets(word))               # 検索語wordの位置情報を得る
