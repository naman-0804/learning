import streamlit as st
import pandas as pd
import nltk

# Download NLTK resources BEFORE importing modules that use them
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

from src.preprocessing import clean_review, lemmatize_words
from src.model import SentimentModel

@st.cache_resource
def load_model():
    return SentimentModel("data/all_kindle_review.csv")

model = load_model()

st.title("Kindle Review Sentiment Analysis")

st.write("Enter your Kindle review below:")

review_1 = st.text_area("Review 1")
review_2 = st.text_area("Review 2")

if st.button("Analyze Sentiment"):
    if review_1:
        # We clean the review first based on your preprocessing logic
        cleaned_1 = lemmatize_words(clean_review(review_1))
        
        bow_label_1 = "positive" if model.predict_bow(cleaned_1) == 1 else "negative"
        tfidf_label_1 = "positive" if model.predict_tfidf(cleaned_1) == 1 else "negative"
        w2v_label_1 = "positive" if model.predict_w2v(cleaned_1) == 1 else "negative"
        
        st.write(f"\n**Review 1:** {review_1}")
        st.write(f"  **BOW:** {bow_label_1}")
        st.write(f"  **TF-IDF:** {tfidf_label_1}")
        st.write(f"  **Word2Vec:** {w2v_label_1}")

    if review_2:
        cleaned_2 = lemmatize_words(clean_review(review_2))
        
        bow_label_2 = "positive" if model.predict_bow(cleaned_2) == 1 else "negative"
        tfidf_label_2 = "positive" if model.predict_tfidf(cleaned_2) == 1 else "negative"
        w2v_label_2 = "positive" if model.predict_w2v(cleaned_2) == 1 else "negative"
        
        st.write(f"\n**Review 2:** {review_2}")
        st.write(f"  **BOW:** {bow_label_2}")
        st.write(f"  **TF-IDF:** {tfidf_label_2}")
        st.write(f"  **Word2Vec:** {w2v_label_2}")