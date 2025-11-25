# Deployment Guide for CPU RAG Pipeline
1. pip install -r requirements.txt
2. Add GGML LLM into models/
3. python src/ingest.py
4. uvicorn app.api:app --reload
