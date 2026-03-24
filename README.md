# 🔐 Role-Based RAG Chatbot

A secure AI chatbot that uses **Retrieval-Augmented Generation (RAG)** with **Role-Based Access Control (RBAC)** to ensure users only access authorized information.

---

## 🚀 Features

- 🔐 Role-Based Access Control (RBAC)
- 🧠 Retrieval-Augmented Generation (RAG)
- 📄 Supports CSV + Markdown data
- ⚡ FastAPI backend
- 🎯 ChromaDB vector database
- 🤖 Gemini LLM integration
- 🌐 Streamlit interactive UI
- 👤 Real employee-based login system

---

## 🏗️ Architecture

```text
User → Authentication → RBAC → Vector Search → LLM → Response
