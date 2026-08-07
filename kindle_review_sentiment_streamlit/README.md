# Kindle Review Sentiment Analysis

This project is a Streamlit application for performing sentiment analysis on Kindle reviews. It utilizes various natural language processing techniques to classify reviews as positive or negative based on user input.

## Project Structure

```
kindle_review_sentiment_streamlit
├── app.py                  # Main entry point for the Streamlit application
├── requirements.txt        # Lists project dependencies
├── README.md               # Documentation for the project
├── data                    # Directory containing the dataset
│   └── all_kindle_review.csv  # Dataset of Kindle reviews
└── src                     # Source code for the application
    ├── __init__.py        # Marks the src directory as a Python package
    ├── preprocessing.py    # Functions for data preprocessing
    ├── model.py            # Model definitions and prediction functions
    └── utils.py            # Utility functions for the project
```

## Installation

To run this application, you need to have Python installed on your machine. Follow these steps to set up the project:

1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Install the required dependencies using pip:

   ```
   pip install -r requirements.txt
   ```

## Running the Application

To start the Streamlit application, run the following command in your terminal:

```
streamlit run app.py
```

This will launch the application in your default web browser, where you can input Kindle reviews and see the sentiment analysis results.

## Usage

1. Enter a Kindle review in the provided input box.
2. Click the submit button to analyze the sentiment.
3. The application will display whether the review is classified as positive or negative based on the trained models.

## Acknowledgments

This project utilizes various libraries for natural language processing and machine learning, including Streamlit, pandas, and scikit-learn.