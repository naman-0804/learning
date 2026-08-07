import os
import gdown
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

st.set_page_config(page_title="Vehicle Image Classifier")

st.title("Vehicle Image Classifier")
st.write("Upload an image of a vehicle to classify it.")

# ----------------------------
# Download model from Google Drive if not present
# ----------------------------
MODEL_PATH = "vehicle_classifier.keras"
FILE_ID = "1DMCwcFRl2H1JV1xsloRSJChouuHdgLib"

if not os.path.exists(MODEL_PATH):
    with st.spinner("Downloading model... Please wait (first run only)."):
        url = f"https://drive.google.com/uc?id={FILE_ID}"
        gdown.download(url, MODEL_PATH, quiet=False)

# ----------------------------
# Load model
# ----------------------------
@st.cache_resource
def load_model():
    return tf.keras.models.load_model(MODEL_PATH)

try:
    model = load_model()

    class_names = [
        "SUV",
        "bus",
        "family sedan",
        "fire engine",
        "heavy truck",
        "jeep",
        "minibus",
        "racing car",
        "taxi",
        "truck"
    ]

    uploaded_file = st.file_uploader(
        "Choose an image...",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")

        st.image(
            image,
            caption="Uploaded Image",
            use_container_width=True
        )

        img = image.resize((224, 224))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)

        with st.spinner("Classifying..."):
            predictions = model.predict(img_array, verbose=0)

        score = predictions[0]

        st.success(
            f"Prediction: **{class_names[np.argmax(score)]}** "
            f"({100 * np.max(score):.2f}% confidence)"
        )

except Exception as e:
    st.error(f"Error: {e}")