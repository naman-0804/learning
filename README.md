# Next Word Prediction using LSTM (https://next-wordd-prediction.streamlit.app/)

The next step in this project is to build and test an **LSTM-based Next Word Prediction model**.

## Model Training

The model was trained using the following configuration:

- **Architecture:** LSTM
- **Training Samples:** 200
- **Epochs:** 2
- **Batch Size:** 32

The training was intentionally limited to a small number of samples and epochs to reduce training time.

## Important Note

> **The current model is highly imperfect due to system resource limitations.**

To reduce computational requirements, only **200 training samples** were used and the model was trained for just **2 epochs**. Because of this limited training, the model currently has very low accuracy and should be considered a **basic demonstration/prototype rather than a production-quality next-word predictor**.

The low accuracy is expected and does not represent the potential performance of an adequately trained LSTM model with sufficient data, epochs, and computational resources.
