from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from backend.pdf_processing import process_pdf, store_embeddings

# Load the textbook and store embeddings (only needs to be done once)
def setup_knowledge_base(pdf_path):
    docs = process_pdf(pdf_path)
    store_embeddings(docs)

# Initialize the RAG pipeline
def ask_question(query):
    retriever = Pinecone.from_existing_index(index_name="nelson-pediatrics").as_retriever(search_kwargs={"k": 3})
    qa_chain = RetrievalQA.from_chain_type(llm=OpenAI(temperature=0), retriever=retriever)
    return qa_chain.run(query)