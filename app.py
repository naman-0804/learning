import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import os

st.title("Vehicle Image Classifier")
st.write("Upload an image of a vehicle to classify it.")

model_path = "vehicle_classifier.keras"

# Check if model exists, since it wasn't saved in the notebook
if not os.path.exists(model_path):
    st.warning(f"Model file '{model_path}' not found! ⚠️")
    st.info("Please go back to your `cnn_vehicle.ipynb` notebook and save your trained model by adding this line at the end:\n\n`model.save('vehicle_classifier.keras')`")
else:
    # Load model
    @st.cache_resource
    def load_model():
        return tf.keras.models.load_model(model_path)
    
    try:
        model = load_model()
        
        # Class names from your dataset
        class_names = ['SUV', 'bus', 'family sedan', 'fire engine', 'heavy truck', 'jeep', 'minibus', 'racing car', 'taxi', 'truck']
        
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
        
        if uploaded_file is not None:
            # Display uploaded image
            image = Image.open(uploaded_file).convert('RGB')
            st.image(image, caption='Uploaded Image', use_container_width=True)
            st.write("Classifying...")
            
            # Preprocess the image to match training (224x224)
            img = image.resize((224, 224))
            img_array = tf.keras.preprocessing.image.img_to_array(img)
            img_array = tf.expand_dims(img_array, 0) # Create a batch
            
            # Predict
            predictions = model.predict(img_array)
            # The model already has a softmax layer, so predictions are probabilities
            score = predictions[0]
            
            st.success(
                "Prediction: **{}** ({:.2f}% confidence)"
                .format(class_names[np.argmax(score)], 100 * np.max(score))
            )
            
    except Exception as e:
        st.error(f"An error occurred: {e}")
