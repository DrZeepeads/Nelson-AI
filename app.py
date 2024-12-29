import streamlit as st
from backend.qa_pipeline import ask_question

# Streamlit configuration
st.set_page_config(page_title="NelsonGPT", page_icon="🩺")

# Application title
st.title("NelsonGPT: Pediatric Knowledge Assistant")

# Sidebar
st.sidebar.title("About")
st.sidebar.info(
    """
    **NelsonGPT** is a chatbot powered by AI and the *Nelson Textbook of Pediatrics*. 
    Ask questions related to symptoms, diagnoses, treatments, or developmental milestones.
    """
)

# Input box for user queries
query = st.text_input("Ask your question:")

if query:
    # Call the backend to get an answer
    answer = ask_question(query)
    
    # Display the answer
    st.write("### Answer:")
    st.write(answer)
