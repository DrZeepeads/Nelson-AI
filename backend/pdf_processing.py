from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

# Load and process the PDF
def process_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    # Split document into smaller chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = splitter.split_documents(documents)

    return docs

# Generate and store embeddings using FAISS
def store_embeddings(docs):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = [model.encode(doc.page_content) for doc in docs]

    # Initialize FAISS
    dimension = len(embeddings[0])
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))

    return index, docs