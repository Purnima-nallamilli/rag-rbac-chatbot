from fastapi import FastAPI
from backend.auth import get_user_role   
from backend.rag_pipeline import get_response

app = FastAPI()


@app.post("/chat")
def chat(username: str, query: str):
    try:
        # 🔐 Authenticate user
        role = get_user_role(username)

        # 🧠 Get response from RAG
        result = get_response(query, role)

        return {
            "role": role,
            "answer": result["answer"],
            "sources": result["sources"]
        }

    except ValueError as e:
        return {"error": str(e)}

    except Exception as e:
        return {"error": f"Something went wrong: {str(e)}"}