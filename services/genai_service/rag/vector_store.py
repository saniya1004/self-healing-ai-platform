import faiss
import numpy as np
from .embedder import get_embedding

dimension = 384
index = faiss.IndexFlatL2(dimension)

documents = []
doc_embeddings = []

def add_documents(texts):
    global documents, doc_embeddings

    for text in texts:
        emb = get_embedding(text)
        documents.append(text)
        doc_embeddings.append(emb)

    index.add(np.array(doc_embeddings).astype("float32"))

def search(query, k=2):
    query_emb = np.array([get_embedding(query)]).astype("float32")
    distances, indices = index.search(query_emb, k)

    results = [documents[i] for i in indices[0]]
    return results

add_documents([
    "API stands for Application Programming Interface.",
    "Machine learning is a subset of artificial intelligence.",
    "FastAPI is a Python framework for building APIs.",
    "Databases store structured information."
])