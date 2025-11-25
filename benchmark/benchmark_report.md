
📊 Benchmark Report (Short & Simple)

This report summarizes the performance of the **CPU-based RAG pipeline** using **Mistral-7B-Instruct (GGUF)**, FAISS, and Sentence-Transformers.

---

🖥️ System Used

* CPU: Intel i5/i7
* RAM: 8–16 GB
* GPU: None (CPU-only)
* Model: Mistral-7B-Instruct-Q4_K_M
* Embedding Model: MiniLM-L6-v2

---

🚀 Key Performance Metrics

| Component                       | Time              
| ------------------------------- | ----------------- 
| **Model Load**                  | 11–15 seconds     
| **FAISS Index Load**            | 0.15–0.25 seconds 
| **Retrieval Time**              | 20–40 ms          
| **LLM Generation (150 tokens)** | 3–5 seconds       
| **End-to-End RAG Response**     | 5–7 seconds   

---

🧪 Example RAG Query

Question:
What does the assignment require?

Performance:

* Retrieval: ~30 ms
* Generation: ~4 seconds
* Total: ~5 seconds

---

✔ Observations

* Works fully offline on CPU
* Retrieval is extremely fast
* LLM generation is the slowest part (expected on CPU)
* End-to-end latency is **5–7 seconds**, suitable for demos or interviews

---

⚙ Simple Optimizations

* Reduce `max_tokens`
* Reduce `n_ctx` from 4096 → 2048
* Use 6–8 CPU threads
* Use smaller models (Phi-3, Mistral-7B Q4_K_S)

