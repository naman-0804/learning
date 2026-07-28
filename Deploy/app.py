import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# -----------------------------
# Load Model
# -----------------------------
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("vehicle_classifier.keras")

model = load_model()

# -----------------------------
# Class Names
# -----------------------------
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

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Vehicle Classifier", page_icon="🚗")

st.title("🚗 Vehicle Classification using CNN")
st.write("Upload an image of a vehicle.")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Preprocess
    image = image.resize((224, 224))

    img_array = np.array(image, dtype=np.float32)
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    prediction = model.predict(img_array, verbose=0)

    predicted_index = np.argmax(prediction)
    confidence = float(np.max(prediction) * 100)

    st.success(f"Prediction: **{class_names[predicted_index]}**")
    st.write(f"Confidence: **{confidence:.2f}%**")

    st.subheader("Prediction Probabilities")

    for cls, prob in zip(class_names, prediction[0]):
        st.progress(float(prob))
        st.write(f"{cls}: {prob*100:.2f}%")