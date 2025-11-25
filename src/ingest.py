from sentence_transformers import SentenceTransformer
from pypdf import PdfReader
import faiss, json, os

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

reader = PdfReader("data/docs/AI_ML Assignment.pdf")

# Extract each page separately
docs = [(p.extract_text() or "") for p in reader.pages]

# Encode all pages
embeddings = model.encode(docs)

dim = embeddings.shape[1]
index = faiss.IndexFlatL2(dim)
index.add(embeddings)

os.makedirs("embeddings", exist_ok=True)

faiss.write_index(index, "embeddings/faiss.index")
json.dump(docs, open("embeddings/docs.json", "w"))

print("Ingest complete. Pages:", len(docs))
