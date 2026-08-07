import numpy as np
import os
import joblib

class SentimentModel:
    def __init__(self, data_dir):
        # Load all pre-trained models from the data directory
        self.bow_vectorizer = joblib.load(os.path.join(data_dir, 'bow_vectorizer.pkl'))
        self.bow_model = joblib.load(os.path.join(data_dir, 'bow_model.pkl'))
        
        self.tfidf_vectorizer = joblib.load(os.path.join(data_dir, 'tfidf_vectorizer.pkl'))
        self.tfidf_model = joblib.load(os.path.join(data_dir, 'tfidf_model.pkl'))
        
        self.w2v_model = joblib.load(os.path.join(data_dir, 'w2v_model.pkl'))
        self.w2v_classifier = joblib.load(os.path.join(data_dir, 'w2v_classifier.pkl'))

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
        return self.w2v_classifier.predict(vec)[0]