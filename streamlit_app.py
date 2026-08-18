import streamlit as st
import os
from typing import Annotated, TypedDict
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_core.tools import create_retriever_tool
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition

# Streamlit Page Config
st.set_page_config(page_title="Agentic RAG", page_icon="🤖")
st.title("LangChain & LangGraph Agentic RAG")

# API Key and Model configuration at the top
col1, col2 = st.columns(2)
with col1:
    api_key = st.text_input("Enter Gemini API Key", type="password")
with col2:
    model_name = st.selectbox(
        "Select Gemini Model", 
        ("gemini-1.5-flash", "gemini-1.5-pro", "gemini-1.0-pro", "gemini-3.6-flash")
    )

@st.cache_resource(show_spinner=False)
def setup_tools(_api_key):
    # Load LangGraph Docs
    lg_urls = [
        "https://docs.langchain.com/oss/python/langgraph/overview",
        "https://docs.langchain.com/oss/python/langgraph/workflows-agents",
        "https://docs.langchain.com/oss/python/langgraph/graph-api#map-reduce-and-the-send-api"
    ]
    lg_docs = WebBaseLoader(lg_urls).load()
    
    # Load LangChain Docs
    lc_urls = [
        "https://docs.langchain.com/oss/python/langchain/overview",
        "https://docs.langchain.com/oss/python/langchain/models"
    ]
    lc_docs = WebBaseLoader(lc_urls).load()

    # Split documents
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    lg_splits = text_splitter.split_documents(lg_docs)
    lc_splits = text_splitter.split_documents(lc_docs)

    # Embeddings & Vectorstores
    embeddings = GoogleGenerativeAIEmbeddings(model='models/gemini-embedding-2', api_key=_api_key)
    lg_vectorstore = FAISS.from_documents(lg_splits, embeddings)
    lc_vectorstore = FAISS.from_documents(lc_splits, embeddings)

    # Tools
    lg_tool = create_retriever_tool(
        lg_vectorstore.as_retriever(), 
        "retriever_vector_Db_langgraph", 
        "Search information about LangGraph"
    )
    lc_tool = create_retriever_tool(
        lc_vectorstore.as_retriever(), 
        "retriever_vector_Db_langchain", 
        "Search information about LangChain"
    )
    
    return [lg_tool, lc_tool]

# State definition
class State(TypedDict):
    messages: Annotated[list, add_messages]

@st.cache_resource(show_spinner=False)
def get_graph(_api_key, _model_name, _tools):
    def call_model(state: State):
        llm = ChatGoogleGenerativeAI(model=_model_name, api_key=_api_key).bind_tools(_tools)
        response = llm.invoke(state["messages"])
        return {"messages": [response]}

    workflow = StateGraph(State)
    workflow.add_node("agent", call_model)
    workflow.add_node("tools", ToolNode(_tools))
    workflow.add_edge(START, "agent")
    workflow.add_conditional_edges("agent", tools_condition)
    workflow.add_edge("tools", "agent")
    
    return workflow.compile()

# Main app logic
if api_key:
    with st.spinner("Setting up knowledge bases... This might take a moment on first run."):
        tools = setup_tools(api_key)
        app = get_graph(api_key, model_name, tools)

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # React to user input
    if prompt := st.chat_input("Ask a question about LangChain or LangGraph"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("assistant"):
            with st.spinner("Thinking & Searching..."):
                # Invoke LangGraph
                inputs = {"messages": [("user", prompt)]}
                result = app.invoke(inputs)
                
                final_response = result["messages"][-1].content
                
                # Check message history to see if any tools were used
                used_tools = []
                for msg in result["messages"]:
                    if msg.type == "tool":
                        used_tools.append(msg.name)
                
                # Determine which databases were searched
                output_text = final_response
                if used_tools:
                    unique_tools = list(set(used_tools))
                    db_names = []
                    for t in unique_tools:
                        if "langgraph" in t:
                            db_names.append("🛠️ **LangGraph DB**")
                        elif "langchain" in t:
                            db_names.append("🛠️ **LangChain DB**")
                        else:
                            db_names.append(f"🛠️ **{t}**")
                            
                    output_text += f"\n\n---\n*Agent relied on context from: {', '.join(db_names)}*"

                st.markdown(output_text)
                st.session_state.messages.append({"role": "assistant", "content": output_text})
else:
    st.info("Please enter your Gemini API key at the top to start.")
