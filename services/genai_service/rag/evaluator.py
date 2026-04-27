from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from services.genai_service.router import llm_router

response = llm_router(prompt)
model = SentenceTransformer("all-MiniLM-L6-v2")

def compute_similarity(response: str, context_list: list):
    if response is None:
        return 0.0

    # Combine context into one string
    context = " ".join(context_list)

    response_emb = model.encode([response])
    context_emb = model.encode([context])

    score = cosine_similarity(response_emb, context_emb)[0][0]

    return float(score)