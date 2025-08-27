import streamlit as st
import requests


url="http://127.0.0.1:8000/text-response/query"
st.sidebar.title("Sidebar Title")

st.set_page_config(page_title="RAG Chat", layout="wide")

st.title("📚 RAG Assistant")

# Inject custom CSS for right-aligning user messages
st.markdown("""
    <style>
    .user-message {
        background-color: #4CAF50;
        color: white;
        padding: 10px 15px;
        border-radius: 12px;
        margin: 8px 0;
        text-align: right;
        display: inline-block;
        float: right;
        clear: both;
        max-width: 70%;
        word-wrap: break-word;
    }
    .assistant-message {
        background-color: #2d2d2d;
        color: white;
        padding: 10px 15px;
        border-radius: 12px;
        margin: 8px 0;
        text-align: left;
        display: inline-block;
        float: left;
        clear: both;
        max-width: 70%;
        word-wrap: break-word;
    }
    </style>
""", unsafe_allow_html=True)

# Session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Render chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='user-message'>{msg['content']}</div>", unsafe_allow_html=True)
    else:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
    #     st.markdown(f"<div class='assistant-message'>{msg['content']}</div>", unsafe_allow_html=True)

# Input at bottom
if prompt := st.chat_input("Type your question..."):
    # Save and display user msg
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Dummy RAG response (swap with pipeline)
    response = requests.post(url,json={"query":prompt}).json()
    st.session_state.messages.append({"role": "assistant", "content": response["answer"]})

    st.rerun()
    
