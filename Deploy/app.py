import gradio as gr
import tensorflow as tf
import numpy as np
from PIL import Image

# Load model
model = tf.keras.models.load_model("vehicle_classifier.keras")

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

def predict(image):
    image = image.convert("RGB")
    image = image.resize((224, 224))

    img_array = np.array(image, dtype=np.float32)
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array, verbose=0)

    index = np.argmax(prediction)
    confidence = float(prediction[0][index]) * 100

    return f"Prediction: {class_names[index]}\nConfidence: {confidence:.2f}%"

demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs=gr.Textbox(label="Prediction"),
    title="Vehicle Classifier",
    description="Upload a vehicle image."
)

demo.launch()