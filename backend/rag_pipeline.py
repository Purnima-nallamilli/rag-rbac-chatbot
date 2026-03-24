import os
from dotenv import load_dotenv     #ragpipeline.py file#
from google import genai

from backend.vector_store import load_vector_db
from backend.rbac import get_allowed_departments

# 🔹 Load environment variables
load_dotenv()

# 🔹 Initialize Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# 🔹 Load vector database
db = load_vector_db()


def get_response(query, role):
    # 🔐 RBAC: Get allowed departments
    allowed_depts = get_allowed_departments(role)

    # 🔍 Retrieve documents
    docs = db.similarity_search(query, k=20)

    # 🔐 Filter documents based on role
    filtered_docs = [
        doc for doc in docs
        if doc.metadata.get("department") in allowed_depts
    ]

    # ❗ If no access
    if not filtered_docs:
        return {
            "answer": "No access or data not available for your role.",
            "sources": []
        }

    # 🧠 Create context
    context = "\n".join([doc.page_content for doc in filtered_docs])

    # 🤖 Improved Prompt
    prompt = f"""
You are a helpful assistant.

Answer the question using ALL relevant information from the context.

If the question asks for multiple components or layers,
make sure to include ALL of them in your answer.

Do not give partial answers.

Context:
{context}

Question:
{query}
"""

    # 🔥 Generate response using Gemini
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    # ✅ Extract answer safely
    answer = getattr(response, "text", "Error generating response")

    return {
        "answer": answer,
        "sources": [doc.metadata for doc in filtered_docs]
    }