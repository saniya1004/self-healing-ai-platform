# 🚀 Self-Healing AI Platform (GenAI Infra Project)

An intelligent AI system that detects failures in LLM responses and automatically recovers using fallback strategies such as local models and retrieval augmentation.

> Built with a production-style architecture focusing on **GenAI infrastructure**, **resilience**, and **observability**.

---

## 🧠 Problem Statement

LLM-based systems in production often fail due to:
- API quota exhaustion (429 errors)
- Rate limits
- Hallucinations
- Unreliable responses

This project solves that by introducing a **self-healing layer** between the user and the LLM.

---

## 🏗️ Architecture
User
↓
FastAPI Gateway
↓
LLM Router
├── OpenAI (Primary)
└── Ollama (Fallback - Local LLM)
↓
RAG Pipeline (Context Injection)
↓
Evaluator (Quality Check)
↓
Self-Healing Layer (Retry / Fallback)
↓
Final Response


---

## ⚙️ Tech Stack

- **Backend:** FastAPI
- **LLMs:**
  - OpenAI (GPT-4o-mini)
  - Ollama (Local - Gemma / LLaMA)
- **RAG:**
  - FAISS (Vector Store)
  - Sentence Transformers
- **Monitoring:**
  - Custom Logging
  - Evaluation Scoring
- **Language:** Python 3.13

---

## ✨ Features

### ✅ Phase 1 (Completed)
- FastAPI API Gateway
- LLM integration (OpenAI)
- Modular service-based architecture

### ✅ Phase 2 (In Progress)
- RAG pipeline (FAISS + embeddings)
- Context-aware response generation
- Local LLM fallback (Ollama)

### 🔄 Self-Healing System
- Detects:
  - API failures (quota, rate limit)
  - Low-quality responses
- Automatically:
  - Retries
  - Switches to fallback LLM
  - Uses RAG for better answers

---

## 🔥 Example Flow

1. User sends query → `/query`
2. OpenAI is called
3. If:
   - ❌ quota exceeded → fallback to Ollama
   - ❌ poor response → retry / enhance via RAG
4. Final response returned

---

## 🧪 How to Run Locally

### 1. Clone repo
```bash
git clone https://github.com/saniya1004/self-healing-ai-platform.git
cd self-healing-ai-platform


