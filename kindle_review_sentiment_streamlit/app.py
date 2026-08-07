import streamlit as st
import pandas as pd
from src.preprocessing import clean_review, lemmatize_words
from src.model import predict_sentiment_bow, predict_sentiment_tfidf, predict_sentiment_w2v
import nltk
# Download NLTK resources (it will only download if it hasn't already)
nltk.download('stopwords')

# Depending on your code, you might also need these:
nltk.download('punkt')
nltk.download('wordnet')

st.title("Kindle Review Sentiment Analysis")

st.write("Enter your Kindle review below:")

review_1 = st.text_area("Review 1")
review_2 = st.text_area("Review 2")

if st.button("Analyze Sentiment"):
    if review_1:
        bow_label_1 = "positive" if predict_sentiment_bow(review_1) == 1 else "negative"
        tfidf_label_1 = "positive" if predict_sentiment_tfidf(review_1) == 1 else "negative"
        w2v_label_1 = "positive" if predict_sentiment_w2v(review_1) == 1 else "negative"
        
        st.write(f"\n**Review 1:** {review_1}")
        st.write(f"  **BOW:** {bow_label_1}")
        st.write(f"  **TF-IDF:** {tfidf_label_1}")
        st.write(f"  **Word2Vec:** {w2v_label_1}")

    if review_2:
        bow_label_2 = "positive" if predict_sentiment_bow(review_2) == 1 else "negative"
        tfidf_label_2 = "positive" if predict_sentiment_tfidf(review_2) == 1 else "negative"
        w2v_label_2 = "positive" if predict_sentiment_w2v(review_2) == 1 else "negative"
        
        st.write(f"\n**Review 2:** {review_2}")
        st.write(f"  **BOW:** {bow_label_2}")
        st.write(f"  **TF-IDF:** {tfidf_label_2}")
        st.write(f"  **Word2Vec:** {w2v_label_2}")