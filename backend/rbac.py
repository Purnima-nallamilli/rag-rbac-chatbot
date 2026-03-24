# 🔐 Role-Based Access Control (RBAC)

# Define which departments each role can access
role_permissions = {
    "finance": ["finance","general"],
    "hr": ["hr","general"],
    "marketing": ["marketing","general"],
    "engineering": ["engineering","general"],
    "admin": ["finance", "hr", "marketing", "engineering", "general"],
    "employee": ["general"]
}


def get_allowed_departments(role: str):
    """
    Returns list of departments the given role can access.
    """

    allowed = role_permissions.get(role)

    if not allowed:
        raise ValueError(f"Invalid role: {role}")

    return allowed