from services.genai_service.llm import generate_response
from services.genai_service.rag.retriever import retrieve_context
from services.genai_service.rag.evaluator import compute_similarity
from services.genai_service.llm import generate_response
from services.genai_service.rag.retriever import retrieve_context
from services.genai_service.rag.evaluator import compute_similarity

def recover_if_needed(query: str, response: str):

    #  Case 1: LLM failed
    if response is None:
        return f"[FALLBACK RESPONSE] Unable to fetch from LLM. Answer: {query}"

    #  Step 2: Retrieve context
    context = retrieve_context(query)

    # Step 3: Evaluate grounding
    score = compute_similarity(response, context)

    print(f"[EVAL SCORE]: {score}")

    # Step 4: Detect hallucination
    if score < 0.5:
        print("[WARNING] Hallucination detected. Retrying...")

        improved_prompt = f"Answer strictly using facts: {query}"
        retry = generate_response(improved_prompt)

        if retry:
            return retry

        return "[SAFE FALLBACK] Could not verify answer."

    return response
