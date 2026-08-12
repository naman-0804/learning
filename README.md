# 1. Smart ATS Resume Analyzer

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ats-scanner-llm.streamlit.app/)

Smart ATS Resume Analyzer is a powerful Streamlit web application that leverages Google's Gemini 3.5 Flash Generative AI model to evaluate resumes against job descriptions. It acts as an Applicant Tracking System (ATS) expert, providing actionable insights to help job seekers optimize their resumes.

## Features

*   **Smart Parsing**: Uses `PyMuPDF` to read and convert PDF resumes into processable image formats.
*   **Gemini AI Integration**: Uses `gemini-3.5-flash` to comprehensively analyze the resume.
*   **Three Evaluation Modes**:
    *   **What to Change / Improve**: Recommends specific skills to focus on, formatting changes, and content additions/removals based on the job description or in general.
    *   **How is my Resume?**: Provides a professional HR-style evaluation, highlighting strengths, weaknesses, and overall alignment with the role.
    *   **Percentage Match**: Calculates an ATS match percentage between the resume and the provided Job Description, highlighting missing keywords.
*   **Secure API Key Usage**: Users securely input their own Google Gemini API key during the session.

## Demo

Check out the live application here: [ATS Scanner LLM on Streamlit](https://ats-scanner-llm.streamlit.app/)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ats-scanner-llm.git
   cd ats-scanner-llm
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run ats_system.py
   ```

## Usage

1. Open the web app.
2. Enter your Google Gemini API Key.
3. Paste the Job Description (optional for general evaluation, required for Percentage Match).
4. Upload your resume in PDF format.
5. Choose one of the evaluation buttons to get your results.

---

# 2. GenAI Q&A Chatbot

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://self-gpt.streamlit.app/)

A simple and interactive conversational AI chatbot built with Streamlit and Google's Gemini 3.5 Flash Generative AI model. 

## Features

*   **Interactive Chat Interface**: A seamless and user-friendly chat UI built directly into Streamlit.
*   **Gemini AI Integration**: Powered by `gemini-3.5-flash` for fast, intelligent, and accurate responses.
*   **Chat History**: Automatically stores and displays previous messages in the session using Streamlit's `session_state`.
*   **Secure API Key Usage**: Allows users to input their personal Google Gemini API key securely to start chatting.

## Demo

Check out the live application here: [Self-GPT on Streamlit](https://self-gpt.streamlit.app/)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/self-gpt.git
   cd self-gpt
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run qachat.py
   ```

## Usage

1. Open the web app.
2. Enter your Google Gemini API Key in the designated field.
3. Type a question or prompt in the chat input at the bottom of the page and hit Enter.
4. Interact with the Gemini AI and view your conversation history on the screen.
