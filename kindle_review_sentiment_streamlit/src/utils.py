def clean_review(text):
    import re
    import html
    from nltk.corpus import stopwords

    stopwords_set = set(stopwords.words('english'))

    if pd.isna(text):
        return ""
    text = text.lower()
    text = html.unescape(text)
    text = re.sub(r'http\S+|www\.\S+|ftp\S+', " ", text)
    text = re.sub(r'<.*?>', " ", text)
    text = re.sub(r'[^a-z\s]', " ", text)
    text = re.sub(r'\s+', " ", text).strip()
    return " ".join(word for word in text.split() if word not in stopwords_set)

def lemmatize_words(text):
    from nltk.stem import WordNetLemmatizer
    lemmatizer = WordNetLemmatizer()
    return " ".join([lemmatizer.lemmatize(word) for word in text.split()])