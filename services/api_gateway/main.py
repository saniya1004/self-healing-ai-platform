from fastapi import FastAPI
from pydantic import BaseModel
from services.genai_service.router import llm_router
from services.ml_service.model import predict
from services.monitoring_service.logger import log_event
from services.self_healing_service.healer import recover_if_needed

app = FastAPI()

class Query(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Self-Healing AI Platform Running"}

@app.post("/query")
def query_llm(q: Query):
    result = llm_router(q.text)

    return {
        "original": q.text,
        "final": result
    }

    # Self-healing check
    final_response = recover_if_needed(query.text, response)

    return {
        "original": response,
        "final": final_response
    }

@app.get("/predict")
def predict_value(x: float):
    result = predict(x)

    log_event({
        "type": "ml_prediction",
        "input": x,
        "output": result
    })

    return {"prediction": result}