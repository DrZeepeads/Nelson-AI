import streamlit as st
from backend.qa_pipeline import ask_question

# Streamlit configuration
st.set_page_config(
    page_title="NelsonGPT: Pediatric Knowledge Assistant",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main { 
        background-color: #f7f9fc; 
    }
    .stTextInput > div > input {
        border-radius: 8px;
        border: 1px solid #ccc;
        padding: 10px;
        font-size: 1rem;
    }
    .stSidebar .stSidebarContent {
        background-color: #eef2f6;
        padding: 20px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Application title
st.title("🩺 NelsonGPT: Pediatric Knowledge Assistant")
st.markdown("#### Your trusted AI companion for pediatric care!")

# Sidebar content
st.sidebar.title("📖 About NelsonGPT")
st.sidebar.info(
    """
    **NelsonGPT** is a chatbot powered by AI and the *Nelson Textbook of Pediatrics*.  
    Ask questions related to:
    - Symptoms  
    - Diagnoses  
    - Treatments  
    - Developmental milestones  
    """
)
st.sidebar.markdown("---")
st.sidebar.title("🔗 Resources")
st.sidebar.markdown("[Nelson Textbook of Pediatrics](https://www.elsevier.com/)")  # Example link

# Input box for user queries
st.markdown("### Ask your question below:")
query = st.text_input(
    "",
    placeholder="Type your question here, e.g., 'What are the symptoms of measles?'",
    help="Ask anything related to pediatrics, symptoms, treatments, or diagnoses."
)

# Submit button
if query:
    with st.spinner("Processing your query..."):
        try:
            # Call the backend to get an answer
            answer = ask_question(query)

            # Display the answer
            st.success("### Answer:")
            st.write(answer)
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Footer
st.markdown("---")
st.markdown(
    """
    *Developed by Pediatric AI Solutions.*  
    For questions or feedback, contact us at [support@example.com](mailto:support@example.com).
    """
)
