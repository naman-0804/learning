import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

model = tf.keras.models.load_model("/workspace/Deploy/vehicle_classifier.keras")

class_names = ['SUV',
 'bus',
 'family sedan',
 'fire engine',
 'heavy truck',
 'jeep',
 'minibus',
 'racing car',
 'taxi',
 'truck']

st.title("Image Classifier")

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image)

    image = image.resize((224, 224))
    image = np.expand_dims(image, axis=0)

    prediction = model.predict(image)
    index = np.argmax(prediction)

    st.success(f"Prediction: {class_names[index]}")