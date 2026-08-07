from sklearn.naive_bayes import MultinomialNB, GaussianNB
import numpy as np
import pandas as pd
from gensim.models import Word2Vec
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

class SentimentModel:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path, encoding='utf-8')
        self.bow_vectorizer = CountVectorizer()
        self.tfidf_vectorizer = TfidfVectorizer()
        self.w2v_model = None
        self.bow_model = None
        self.tfidf_model = None
        self._prepare_data()

    def _prepare_data(self):
        self.data['rating'] = self.data['rating'].apply(lambda x: 0 if x < 3 else 1)
        self.data['reviewText'] = self.data['reviewText'].str.lower()
        self.data['reviewText'] = self.data['reviewText'].str.replace(r'http\S+|www\.\S+|ftp\S+', " ", regex=True)
        self.data['reviewText'] = self.data['reviewText'].str.replace(r'[^a-z\s]', " ", regex=True)
        self.data['reviewText'] = self.data['reviewText'].str.replace(r'\s+', " ", regex=True).str.strip()

        self.X = self.data['reviewText']
        self.y = self.data['rating']

        self.bow_vectorizer.fit(self.X)
        self.tfidf_vectorizer.fit(self.X)

        sentences = [text.split() for text in self.X]
        self.w2v_model = Word2Vec(sentences, vector_size=100, window=5, min_count=2, workers=4, epochs=45, seed=42)

        self.bow_model = MultinomialNB().fit(self.bow_vectorizer.transform(self.X).toarray(), self.y)
        self.tfidf_model = MultinomialNB().fit(self.tfidf_vectorizer.transform(self.X).toarray(), self.y)

    def predict_bow(self, text):
        vec = self.bow_vectorizer.transform([text]).toarray()
        return self.bow_model.predict(vec)[0]

    def predict_tfidf(self, text):
        vec = self.tfidf_vectorizer.transform([text]).toarray()
        return self.tfidf_model.predict(vec)[0]

    def document_vector(self, text):
        words = [w for w in text.split() if w in self.w2v_model.wv]
        if not words:
            return np.zeros(self.w2v_model.vector_size)
        return np.mean(self.w2v_model.wv[words], axis=0)

    def predict_w2v(self, text):
        vec = self.document_vector(text).reshape(1, -1)
        return GaussianNB().fit(self.document_vector(self.X).reshape(-1, self.w2v_model.vector_size), self.y).predict(vec)[0]