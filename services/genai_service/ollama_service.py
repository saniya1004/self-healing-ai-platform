import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def call_ollama(prompt: str) -> str:
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "gemma:2b",
                "prompt": prompt,
                "stream": False
            }
        )

        data = response.json()

        return data.get("response", "").strip() or "Ollama returned empty response"

    except Exception as e:
        print(f"[OLLAMA ERROR]: {e}")
        return "[FALLBACK FAILED]"