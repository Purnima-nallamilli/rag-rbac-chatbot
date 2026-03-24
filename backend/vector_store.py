from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# 🔹 Same embedding model used during ingestion
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

def load_vector_db():
    db = Chroma(
        persist_directory="db",
        embedding_function=embeddings
    )
    return db