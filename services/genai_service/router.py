from services.genai_service.llm import generate_response
from services.genai_service.ollama_service import call_ollama

def llm_router(query: str) -> str:
    response = generate_response(query)

    # 🔴 If OpenAI failed → fallback
    if response is None:
        print("[FALLBACK] → Switching to Ollama")
        return call_ollama(query)

    return response