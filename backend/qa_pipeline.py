from transformers import pipeline
from backend.pdf_processing import process_pdf, store_embeddings

# Initialize the retrieval pipeline
docs = process_pdf("data/nelson_textbook_of_pediatrics.pdf")
index, docs = store_embeddings(docs)
qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-small")

# Question-Answering with Retrieval
def ask_question(query):
    # Search for relevant chunks
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer("all-MiniLM-L6-v2")
    query_embedding = model.encode(query)

    import numpy as np
    import faiss
    distances, indices = index.search(np.array([query_embedding]), k=3)
    retrieved_text = "\n".join([docs[i].page_content for i in indices[0]])

    # Pass the retrieved text to the FLAN-T5 model
    prompt = f"Using the following context, answer the question:\n\n{retrieved_text}\n\nQuestion: {query}"
    response = qa_pipeline(prompt)

    return response[0]["generated_text"]