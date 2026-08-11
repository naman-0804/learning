import os
import numpy as np
import streamlit as st

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer


# --------------------------------------------------
# Paths
# --------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "next_word_model.keras"
)

TEXT_PATH = os.path.join(
    BASE_DIR,
    "shakespeare-hamlet.txt"
)

TRAINING_IMAGE_PATH = os.path.join(
    BASE_DIR,
    "training_accuracy.png"
)


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Hamlet Next-Word Predictor",
    layout="centered"
)


# --------------------------------------------------
# Load model
# --------------------------------------------------

@st.cache_resource
def load_next_word_model():

    model = load_model(
        MODEL_PATH,
        compile=False
    )

    return model


# --------------------------------------------------
# Build tokenizer
# --------------------------------------------------

@st.cache_data
def build_tokenizer_and_max_len():

    with open(
        TEXT_PATH,
        "r",
        encoding="utf-8"
    ) as f:

        text = f.read().lower()

    tokenizer = Tokenizer()

    tokenizer.fit_on_texts([text])

    lines = [
        line
        for line in text.split("\n")
        if line.strip()
    ]

    token_lists = [
        tokenizer.texts_to_sequences([line])[0]
        for line in lines
    ]

    max_sequence_len = max(
        (len(tokens) for tokens in token_lists),
        default=1
    )

    return tokenizer, max_sequence_len


# --------------------------------------------------
# Predict next word
# --------------------------------------------------

def predict_next_word(
    model,
    tokenizer,
    text,
    max_sequence_len
):

    token_list = tokenizer.texts_to_sequences(
        [text.lower()]
    )[0]

    if not token_list:

        return (
            "Please enter text that contains "
            "words from the Hamlet dataset."
        )

    token_list = pad_sequences(
        [token_list],
        maxlen=max_sequence_len - 1,
        padding="pre"
    )

    predicted = model.predict(
        token_list,
        verbose=0
    )

    predicted_word_index = np.argmax(
        predicted,
        axis=-1
    )[0]

    for word, index in tokenizer.word_index.items():

        if index == predicted_word_index:

            return word

    return "No prediction available"


# --------------------------------------------------
# Main application
# --------------------------------------------------

def main():

    st.title("Hamlet Next-Word Predictor")

    st.write(
        "Type a partial phrase and the model "
        "will predict the next likely word."
    )

    user_input = st.text_input(
        "Enter prompt",
        value="to be or not to"
    )

    if st.button("Predict next word"):

        with st.spinner(
            "Loading model and generating prediction..."
        ):

            model = load_next_word_model()

            tokenizer, max_sequence_len = (
                build_tokenizer_and_max_len()
            )

            predicted = predict_next_word(
                model,
                tokenizer,
                user_input,
                max_sequence_len
            )

        st.success("Prediction complete")

        st.write(
            f"**Next word:** {predicted}"
        )

    st.markdown("---")

    st.markdown(
        "This app loads `next_word_model.keras` "
        "and uses the Shakespeare Hamlet corpus "
        "to build the tokenizer."
    )

    st.caption(
        "Run with: `streamlit run streamlit/app.py`"
    )

    st.image(
        TRAINING_IMAGE_PATH,
        caption="Training snapshot: final accuracy is 0.05 due to limited system resources.",
        use_column_width=True
    )

    st.write(
        "**Important:** The model accuracy is only 0.05 because the system was not sufficient to fully train the network."
    )


# --------------------------------------------------
# Run application
# --------------------------------------------------

if __name__ == "__main__":
    main()