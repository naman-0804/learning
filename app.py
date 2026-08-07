import os
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import gdown

st.set_page_config(page_title="Vehicle Image Classifier")

st.title("Vehicle Image Classifier")
st.write("Upload an image of a vehicle to classify it.")

# ----------------------------
# Model Configuration
# ----------------------------
MODEL_PATH = "vehicle_classifier.keras"
FILE_ID = "1DMCwcFRl2H1JV1xsloRSJChouuHdgLib"
URL = f"https://drive.google.com/uc?export=download&id={FILE_ID}"

# ----------------------------
# Download model if needed
# ----------------------------
if os.path.exists(MODEL_PATH):
    # Delete corrupted/small file
    if os.path.getsize(MODEL_PATH) < 1000000:
        os.remove(MODEL_PATH)

if not os.path.exists(MODEL_PATH):
    with st.spinner("Downloading model (first run only)..."):
        gdown.download(URL, MODEL_PATH, quiet=False)

# ----------------------------
# Debug Information
# ----------------------------
st.write("Current Directory:", os.getcwd())
st.write("Files:", os.listdir("."))

if os.path.exists(MODEL_PATH):
    st.success("Model file found")
    st.write("Model Size:", os.path.getsize(MODEL_PATH), "bytes")
else:
    st.error("Model download failed.")
    st.stop()

# ----------------------------
# Load Model
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
        img_array = tf.expand_dims(img_array, axis=0)

        with st.spinner("Classifying..."):
            predictions = model.predict(img_array, verbose=0)

        score = predictions[0]
        predicted_class = class_names[np.argmax(score)]
        confidence = np.max(score) * 100

        st.success(
            f"Prediction: **{predicted_class}**\n\nConfidence: **{confidence:.2f}%**"
        )

except Exception as e:
    import traceback

    st.error(f"Error: {type(e).__name__}")
    st.code(str(e))
    st.code(traceback.format_exc())