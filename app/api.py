from fastapi import FastAPI
from src.pipeline import rag
app = FastAPI()
@app.get("/ask")
def ask(q: str):
    return {"query": q, "answer": rag(q)}
