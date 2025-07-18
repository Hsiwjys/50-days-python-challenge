# 🧠 LangChain RAG Toolkit

This project is a **complete Retrieval-Augmented Generation (RAG) pipeline** built with **LangChain**. It includes multiple vector stores, embedding generation, document processing, and a Streamlit/Q&A interface — ready for experimentation and learning.

---

## 📁 Project Structure
langchain_T/
├── chroma_g/ # Vector DB using Chroma
├── documents/ # Raw input documents (PDF, text, etc.)
├── faiss_gemini/ # FAISS-based vector store using Gemini embeddings
├── images/ # Visuals, architecture diagrams, screenshots
├── .env # API keys and environment variables
├── document_loader.ipynb # Load and preview documents
├── Embenddings.ipynb # Generate embeddings (OpenAI/Gemini)
├── Rag_app.py # Streamlit app to run RAG pipeline
├── Rag.ipynb # Fusion & Advanced RAG logic in notebook format
├── retriever.ipynb # Retriever logic from vector DBs
├── text_splitter.ipynb # RecursiveCharacterTextSplitter usage
├── vector_store.ipynb # Pinecone, FAISS, or Chroma vector store setup


---

## 🚀 Features

- 🔍 **Document Loader** — Reads and parses documents for vectorization
- 🧠 **Embeddings** — Supports `OpenAI` and `Gemini` for text embedding
- 📤 **Vector Store Support** — FAISS, Chroma, and Pinecone
- 🔗 **RAG App** — Streamlit frontend to chat with your documents
- 🧪 **Fusion RAG** — Early fusion and reranking-based retrieval
- ⚡ **Modular Notebooks** — Split by logical function for easier understanding

---
