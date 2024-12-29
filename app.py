import streamlit as st
from backend.qa_pipeline import ask_question

# Set page configuration
st.set_page_config(page_title="NelsonGPT", page_icon="🩺", layout="wide")

# App Header
st.title("NelsonGPT: Advanced Pediatric Knowledge Assistant")
st.markdown("Ask questions based on the **Nelson Textbook of Pediatrics**.")

# Persistent session for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Input Section
query = st.text_input("Enter your pediatric question:")
if query:
    with st.spinner("Thinking..."):
        response = ask_question(query)
        st.session_state.messages.append({"query": query, "response": response})
        st.markdown(f"### Answer: {response}")

# Chat History Section
if st.session_state.messages:
    st.markdown("### Chat History")
    for msg in st.session_state.messages:
        st.write(f"**Q:** {msg['query']}")
        st.write(f"**A:** {msg['response']}")

# Download Chat History
if st.session_state.messages:
    history = "\n".join([f"Q: {m['query']}\nA: {m['response']}" for m in st.session_state.messages])
    st.download_button("Download Chat History", history, "chat_history.txt")