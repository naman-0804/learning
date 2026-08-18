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
col1, col2, col3 = st.columns(3)
with col1:
    api_key = st.text_input("Enter Gemini API Key", type="password")
with col2:
    model_name = st.text_input("Enter Gemini Model Name")
with col3:
    embedding_model = st.text_input("Enter Embedding Model")

@st.cache_resource(show_spinner=False)
def setup_tools(api_key, embedding_model):
    # Load LangGraph Docs
    lg_urls = [
        "https://docs.langchain.com/oss/python/langgraph/overview",
    ]
    lg_docs = WebBaseLoader(lg_urls).load()
    
    # Load LangChain Docs
    lc_urls = [
        "https://docs.langchain.com/oss/python/langchain/overview",
    ]
    lc_docs = WebBaseLoader(lc_urls).load()

    # Split documents
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    lg_splits = text_splitter.split_documents(lg_docs)
    lc_splits = text_splitter.split_documents(lc_docs)

    # Embeddings & Vectorstores
    embeddings = GoogleGenerativeAIEmbeddings(model=embedding_model, api_key=api_key)
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
def get_graph(api_key, model_name, _tools):
    def call_model(state: State):
        llm = ChatGoogleGenerativeAI(model=model_name, api_key=api_key).bind_tools(_tools)
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
if api_key and model_name and embedding_model:
    with st.spinner("Setting up knowledge bases... This might take a moment on first run."):
        tools = setup_tools(api_key, embedding_model)
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
                
                final_content = result["messages"][-1].content
                
                # Extract string correctly if the model returned a list of dicts
                if isinstance(final_content, list):
                    text_parts = [part["text"] for part in final_content if isinstance(part, dict) and "text" in part]
                    output_text = "".join(text_parts)
                else:
                    output_text = str(final_content)
                
                # Check message history to see if any tools were used
                used_tools = []
                for msg in result["messages"]:
                    if getattr(msg, "type", "") == "tool":
                        used_tools.append(getattr(msg, "name", "unknown_tool"))
                
                # Determine which databases were searched
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
