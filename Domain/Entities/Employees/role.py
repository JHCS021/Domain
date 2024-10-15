class Role:
    def __init__(self, role_id: int, role_name: str):
        self.role_id = role_id
        self.role_name = role_name

    def __str__(self):
        return f"Role: {self.role_name}"
