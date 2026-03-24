# 👤 Dummy users with roles

users = {
    "finance_user": "finance",
    "hr_user": "hr",
    "marketing_user": "marketing",
    "engineer": "engineering",
    "ceo": "admin",
    "employee": "employee"
}

def get_user_role(username: str):
    role = users.get(username)

    if not role:
        raise ValueError("Invalid username")

    return role