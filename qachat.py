from dotenv import load_dotenv
import os

load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
import streamlit as st
from google import genai

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

chat = client.chats.create(model="gemini-3.5-flash")
def get_gemini_response(question):
    response = chat.send_message(question)
    return response.text

#initialize out streamlit app
st.set_page_config(page_title="Q&A Chatbot")
st.title("Q&A Chatbot")
st.header("Genai LLM Application")
#initialize the chat history

if "chat_history" not in st.session_state:
    st.session_state['chat_history'] = []

# Display chat history
for role, text in st.session_state['chat_history']:
    with st.chat_message("user" if role == "You" else "assistant"):
        st.write(text)

# Input field and message generation
if question := st.chat_input("Ask a question"):
    # Display user's question immediately
    st.session_state['chat_history'].append(("You", question))
    with st.chat_message("user"):
        st.write(question)
    
    # Get Gemini response and display it
    response = get_gemini_response(question)
    st.session_state['chat_history'].append(("Gemini", response))
    with st.chat_message("assistant"):
        st.write(response)
