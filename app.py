import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import os

st.title("Vehicle Image Classifier")
st.write("Upload an image of a vehicle to classify it.")

model_path = "vehicle_classifier.keras"

# Debug information
st.write("Current working directory:", os.getcwd())
st.write("Files in current directory:", os.listdir("."))

if os.path.exists(model_path):
    st.success(f"Found {model_path}")
    st.write("Model size:", os.path.getsize(model_path), "bytes")
else:
    st.error(f"{model_path} NOT FOUND")
    st.stop()


@st.cache_resource
def load_model():
    return tf.keras.models.load_model(model_path)


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
        "truck",
    ]

    uploaded_file = st.file_uploader(
        "Choose an image...",
        type=["jpg", "jpeg", "png"],
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded Image", use_container_width=True)

        img = image.resize((224, 224))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)

        predictions = model.predict(img_array)
        score = predictions[0]

        st.success(
            f"Prediction: {class_names[np.argmax(score)]} "
            f"({100*np.max(score):.2f}% confidence)"
        )

except Exception as e:
    import traceback

    st.error(type(e).__name__)
    st.code(str(e))
    st.code(traceback.format_exc())