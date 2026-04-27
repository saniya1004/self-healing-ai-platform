from .vector_store import search

def retrieve_context(query: str):
    return search(query)