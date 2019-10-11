from nltk.tokenize import word_tokenize
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy

def format_sentense(sentense):
    return {word: True for word in word_tokenize(sentense)}
with open('rt-polarity.pos', encoding='latin-1') as f:
    pos_data = [[format_sentense(line), 'pos'] for line in f]
with open('rt-polarity.neg', encoding='latin-1') as f:
    neg_data = [[format_sentense(line), 'neg'] for line in f]

# 学習データはそれぞれ前半4000文ずつ
training_data = pos_data[:4000] + neg_data[:4000]
# 評価データはそれぞれ4000文以降
testing_data  = pos_data[4000:] + neg_data[4000:]

# training_dataを使って分類木を作る
model = NaiveBayesClassifier.train(train_data)

s1 = 'This is a nice article'
s2 = 'This is a bad article'
print(s1, '--->', model.classify(format_sentense(s1)))  # ２つの文例s1、s2で試す
print(s2, '--->', model.classify(format_sentense(s2)))

print('accuracy', accuracy(model, testing_data))  # testing_dataを使って精度計算
