import streamlit as st
from google import genai

# Initialize our Streamlit app
st.set_page_config(page_title="Q&A Chatbot")

def get_gemini_response(question, api_key):
    if not api_key:
        return "Please enter your API Key above to chat."
    
    client = genai.Client(api_key=api_key)
    chat = client.chats.create(model="gemini-3.5-flash")
    response = chat.send_message(question)
    return response.text

st.title("Q&A Chatbot")
st.header("Genai LLM Application")

api_key = st.text_input("Enter your Google Gemini API Key", type="password")
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
    response = get_gemini_response(question, api_key)
    st.session_state['chat_history'].append(("Gemini", response))
    with st.chat_message("assistant"):
        st.write(response)
