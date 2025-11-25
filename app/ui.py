import streamlit as st
from src.pipeline import rag
st.title("CPU RAG Pipeline")
q = st.text_input("Enter your question")
if st.button("Ask"):
    st.write(rag(q))
