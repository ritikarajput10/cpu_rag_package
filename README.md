# CPU-Optimized RAG LLM — End-to-End Project


🧠 CPU-based RAG Pipeline (PDF Question Answering)

This project implements a complete **Retrieval-Augmented Generation (RAG)** pipeline using:

- PDF ingestion
- SentenceTransformer embeddings
- FAISS vector database
- Local LLM (Mistral 7B Instruct, GGUF) using llama.cpp
- CPU-only execution
- Chat-based question answering

It allows you to upload a PDF and ask questions like:

> “What does the assignment require?”

The model retrieves relevant pages from the PDF and generates an accurate answer.

---

🚀 Features

- Extracts text from PDF page-wise  
- Generates embeddings using `all-MiniLM-L6-v2`  
- Stores vectors using FAISS  
- Loads a local Mistral 7B model via llama.cpp  
- Supports chat-style prompt using built-in template  
- Fully CPU-compatible  
- Clean modular structure (ingest → retrieve → generate → pipeline)

---

🏗 Architecture

                ┌────────────────────────────┐
                │         PDF Document        │
                └───────────────┬────────────┘
                                │
                       (1) Ingestion
                                │
                ┌───────────────▼────────────┐
                │     Sentence Embeddings     │
                └───────────────┬────────────┘
                                │
                     (2) Store in FAISS
                                │
                ┌───────────────▼────────────┐
                │      Vector Database        │
                └───────────────┬────────────┘
                                │
                       (3) Retrieve top-K
                                │
                ┌───────────────▼────────────┐
                │  RAG Prompt Construction    │
                └───────────────┬────────────┘
                                │
                     (4) Generate Answer
                                │
                ┌───────────────▼────────────┐
                │   Local LLM (Mistral 7B)   │
                └────────────────────────────┘



---
📦 Folder Structure

cpu_rag_pipeline/
│
├── data/docs/AI_ML Assignment.pdf
├── embeddings/
│     ├── faiss.index
│     ├── docs.json
│
├── models/mistral-7b-instruct-v0.2.Q4_K_M.gguf
│
├── src/
│   ├── ingest.py
│   ├── retrieve.py
│   ├── generate.py
│   └── pipeline.py
│
└── README.md

````

---
🔧 Installation (Windows)

cd "C:\Users\91637\Downloads\cpu_rag_package\cpu_rag_pipeline"

1. Create environment

python -m venv venv
venv\Scripts\activate


2. Install dependencies

pip install -r requirements.txt


3. Download Mistral Model (GGUF)

## mistral-7b-instruct-v0.2.Q4_K_M.gguf ##

Place it in:

models/




🛠 Step 1 — Build the Vector Store

python src/ingest.py


This will create:

```
embeddings/faiss.index
embeddings/docs.json
```

---

🤖 Step 2 — Run the RAG Chatbot

Mode 1 (recommended)

python -m src.pipeline


Mode 2 (direct)

python src/pipeline.py


---

💬 Usage

```
Ask: What does the assignment require?

Answer: The assignment requires you to...
```

To exit:

exit
quit
CTRL + C


---

🧩 How it Works (RAG Architecture)

1. Ingestion

* PDF → Pages → Text
* Each page is converted into an embedding
* Stored in FAISS + JSON

2. Retrieval

* User question converted into embedding
* FAISS returns top-k similar pages

3. Generation

* Retrieved context passed to Mistral with:


[INST] question + context [/INST]

* Model generates final answer
 


🛠 Technologies Used

* Python
* SentenceTransformers
* FAISS
* Mistral 7B Instruct
* llama.cpp
* PyPDF
* NumPy

---

📝 Future Improvements

* Chunk pages into smaller segments
* Stream output token-by-token
* Add a Gradio UI
* Add PDF upload option
* Evaluate retrieval accuracy

---

👤 Author

Ritika Raj- (MCA) Data Science and AI



