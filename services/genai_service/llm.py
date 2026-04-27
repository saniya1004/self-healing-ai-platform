from openai import OpenAI
import os
from dotenv import load_dotenv
from services.genai_service.rag.retriever import retrieve_context

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_response(query: str):
    try:
        # Retrieve context
        context = retrieve_context(query)

        print("[DEBUG] Retrieved Context:", context)

        # Build prompt
        prompt = f"""
        Answer ONLY using the context below.

        Context:
        {context}

        Question:
        {query}
        """

        # LLM call
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Answer strictly from context."},
                {"role": "user", "content": prompt}
            ]
        )

        final = response.choices[0].message.content

        return final or "No response generated"

    except Exception as e:
        print(f"[OPENAI ERROR]: {e}")
        return None   # allow router to handle fallback