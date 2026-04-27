from services.genai_service.rag.retriever import retrieve_context

query = "What is API?"

results = retrieve_context(query)

print("Retrieved Context:")
for r in results:
    print("-", r)