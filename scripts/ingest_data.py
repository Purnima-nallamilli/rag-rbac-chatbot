import os
import pandas as pd
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma                                      ##ingest_data.py file
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document

DATA_PATH = "resources/data"

# 🔹 Embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)


def load_documents():
    all_docs = []

    for department in os.listdir(DATA_PATH):
        dept_path = os.path.join(DATA_PATH, department)

        if not os.path.isdir(dept_path):
            continue

        for file in os.listdir(dept_path):
            file_path = os.path.join(dept_path, file)

            # ✅ Load Markdown files
            if file.endswith(".md"):
                loader = TextLoader(file_path, encoding="utf-8")
                docs = loader.load()

            # ✅ Load CSV files (FIXED 🔥 using pandas)
            elif file.endswith(".csv"):
                df = pd.read_csv(file_path, sep="\t")  # 🔥 important

                docs = []
                for _, row in df.iterrows():
                    text = "Employee Details:\n"

                    for col in df.columns:
                        text += f"{col}: {row[col]}\n"

                    docs.append(Document(page_content=text))

            else:
                continue

            # ✂️ Split into chunks
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=500,
                chunk_overlap=50
            )

            chunks = splitter.split_documents(docs)

            # 🔐 Add metadata (for RBAC)
            for doc in chunks:
                doc.metadata["department"] = department
                doc.metadata["source"] = file

            all_docs.extend(chunks)

    return all_docs


def store_in_db(documents):
    db = Chroma.from_documents(
        documents,
        embedding=embeddings,
        persist_directory="db"
    )


if __name__ == "__main__":
    docs = load_documents()
    store_in_db(docs)
    print("✅ Data ingestion completed!")