from gensim import corpora, models,  similarities
texts = ["きのう","も","私","は","その","料理","を","食べました"]

# textsを予め準備しておく(分かち書き文のリスト)
num_topics = 3
dictionary = corpora.Dictionary(texts) # 入力textsをdictionaryに変換
corpus = [dictionary.doc2bow(text) for text in texts] # corpusを作成
tfidf = models.TfidfModel(corpus)    # TFIDFモデルを作成
corpus_tfidf = tfidf[corpus]     # corpusをTF-IDFで重要語のみに変換
lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=num_topics) # corpus_tfidfからLSIモデルを作成

# トピックの表示
print(lsi.show_topics(num_topics, formatted=True))  # topicを表示
corpus_lsi = lsi[corpus_tfidf]  # corpus_tfidfのすべての文をLSIに変換
for doc in corpus_lsi:
    x = [sorted(doc, key=lambda u: u[1], reverse=True) for u in doc if len(u)!=0]
    print(x)
