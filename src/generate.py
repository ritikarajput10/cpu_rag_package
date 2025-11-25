# from llama_cpp import Llama
# from retrieve import retrieve

# MODEL_PATH = "models/mistral-7b-instruct-v0.2.Q4_K_M.gguf"

# llm = Llama(
#     model_path=MODEL_PATH,
#     n_ctx=32768,
#     n_threads=6,
#     temperature=0.3
# )

# def rag(query):
#     # Retrieve documents
#     docs = retrieve(query)
#     context = "\n\n".join(docs) if docs else "No context found."

#     messages = [
#         {
#             "role": "user",
#             "content": f"""
# Answer using ONLY the context below:

# Context:
# {context}

# Question: {query}
# """,
#         }
#     ]

#     # IMPORTANT: use chat completion
#     output = llm.create_chat_completion(
#         messages=messages,
#         max_tokens=256,
#     )

#     return output["choices"][0]["message"]["content"].strip()


# # CLI
# if __name__ == "__main__":
#     while True:
#         q = input("Ask: ")
#         print("\nAnswer:\n", rag(q))


from llama_cpp import Llama
from retrieve import retrieve

MODEL_PATH = "models/mistral-7b-instruct-v0.2.Q4_K_M.gguf"

llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=2048,      # Faster and enough for most RAG tasks
    n_threads=6,     # Use your CPU cores
    verbose=False
)

def rag(query):

    # Retrieve fewer documents (speed boost)
    docs = retrieve(query)
    docs = docs[:1]   # take ONLY top 1 (fastest)
    
    context = "\n".join(docs) if docs else "No context found."

    # Mistral v0.2 correct prompt template
    prompt = f"[INST] Use ONLY the context to answer.\n\nContext:\n{context}\n\nQuestion: {query}\nAnswer: [/INST]"

    output = llm(
        prompt,
        max_tokens=120,      # Lower = faster
        temperature=0.2
    )

    return output["choices"][0]["text"].strip()


# CLI
if __name__ == "__main__":
    while True:
        q = input("Ask: ")
        print("\nAnswer:\n", rag(q), "\n")
