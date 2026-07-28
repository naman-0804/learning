# Vehicle Classification using Convolutional Neural Networks (CNN)

A deep learning project that classifies vehicle images into one of ten categories using a custom-built Convolutional Neural Network (CNN) developed with TensorFlow and Keras.

---

## Overview

This project demonstrates the complete workflow of an image classification system:

- Loading and preprocessing image datasets
- Building a custom CNN architecture
- Training and validating the model
- Preventing overfitting using Dropout and Early Stopping
- Evaluating model performance
- Predicting the class of unseen vehicle images

---

## Vehicle Classes

The model classifies images into the following categories:

- SUV
- Bus
- Family Sedan
- Fire Engine
- Heavy Truck
- Jeep
- Minibus
- Racing Car
- Taxi
- Truck

---

## Dataset

**Source:** Kaggle Vehicle Classification Dataset

The dataset is organized into:

```
dataset/
│
├── train/
├── validation/
└── test/
```

Each folder contains one subfolder per vehicle class.

---

## Model Architecture

```
Input Image (224 × 224 × 3)
        │
Rescaling (1/255)
        │
Conv2D (32 Filters, ReLU)
        │
MaxPooling2D
        │
Conv2D (64 Filters, ReLU)
        │
MaxPooling2D
        │
Conv2D (128 Filters, ReLU)
        │
MaxPooling2D
        │
Flatten
        │
Dense (128)
        │
Dropout (0.3)
        │
Dense (10)
        │
Softmax
```

---

## Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Matplotlib
- Scikit-learn

---

## Features

- Custom CNN implementation
- Image preprocessing and normalization
- Early Stopping to reduce overfitting
- Dropout regularization
- Validation accuracy monitoring
- Confusion Matrix
- Classification Report
- Prediction on custom images

---

## Training

The model was trained using:

- Optimizer: Adam
- Loss Function: Sparse Categorical Crossentropy
- Activation Function: ReLU
- Output Activation: Softmax
- Epochs: 20 (with Early Stopping)

---

## Evaluation

The project evaluates performance using:

- Training Accuracy
- Validation Accuracy
- Training Loss
- Validation Loss
- Confusion Matrix
- Precision
- Recall
- F1-Score

---

## Predicting on a New Image

```python
image_path = r"your_image.jpg"
```

The image is:

- Loaded
- Resized to 224×224
- Converted into a tensor
- Passed through the trained CNN
- Predicted using the Softmax output layer

The application displays:

- Predicted Vehicle Class
- Prediction Confidence

---

## Project Structure

```
Vehicle-Classification/
│
├── dataset/
│   ├── train/
│   ├── validation/
│   └── test/
│
├── notebooks/
│   └── vehicle_classification.ipynb
│
├── vehicle_classifier.keras
├── app.py
├── requirements.txt
└── README.md
```

---

## Results

The custom CNN successfully learned to classify ten different vehicle categories from images.

Model performance was analyzed using learning curves, confusion matrix, and classification metrics to understand strengths and common misclassifications between visually similar vehicle classes.

---

## Future Improvements

- Data Augmentation
- Batch Normalization
- Transfer Learning (MobileNetV2, EfficientNet, ResNet)
- Model Quantization
- Web Deployment
- Real-time Webcam Classification
- TensorFlow Lite Deployment

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/vehicle-classification.git
cd vehicle-classification
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python app.py
```

---

## License

This project is intended for educational and learning purposes.
