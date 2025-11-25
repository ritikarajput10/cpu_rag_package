import faiss, json, numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
index = faiss.read_index("embeddings/faiss.index")
docs = json.load(open("embeddings/docs.json"))

def retrieve(query, k=3):
    emb = model.encode([query])
    D, I = index.search(np.array(emb), k)
    return [docs[i] for i in I[0]]
