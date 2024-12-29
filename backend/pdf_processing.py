from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
import pinecone

# Initialize Pinecone
pinecone.init(api_key="your_pinecone_api_key", environment="us-west1-gcp")

# Load the textbook PDF
def process_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    
    # Split the document into smaller chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = splitter.split_documents(documents)
    
    return docs

# Generate and store embeddings
def store_embeddings(docs):
    embeddings = OpenAIEmbeddings()
    vectorstore = Pinecone.from_documents(docs, embeddings, index_name="nelson-pediatrics")
    return vectorstore