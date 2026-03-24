import streamlit as st
import requests

# 🔹 Backend API URL
API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(page_title="RAG RBAC Chatbot", layout="centered")

st.title("🤖 RAG RBAC Chatbot")
st.markdown("Secure role-based AI assistant")

# 🔹 User selection
username = st.selectbox(
    "Select User",
    ["finance_user", "hr_user", "marketing_user", "engineer", "employee", "ceo"]
)

# 🔹 Input
query = st.text_input("Ask your question:")

# 🔹 Button
if st.button("Send"):
    if query:
        with st.spinner("Thinking... 🤔"):
            try:
                response = requests.post(
                    API_URL,
                    params={
                        "username": username,
                        "query": query
                    }
                )

                data = response.json()

                # 🔍 DEBUG (optional, remove later)
                st.write(data)

                # ✅ Correct display
                if "answer" in data:
                    st.success("Answer:")
                    st.write(data["answer"])

                    st.markdown("### 📚 Sources:")
                    for src in data.get("sources", []):
                        st.write(f"- {src}")
                else:
                    st.error(data.get("error", "Something went wrong"))

            except Exception as e:
                st.error(f"Error: {e}")

    else:
        st.warning("Please enter a question")