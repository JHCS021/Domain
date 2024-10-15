# domain/entities/users/user.py

from datetime import datetime

class User:
    def __init__(self, user_id: int, first_name: str, last_name: str, email: str, password: str, role_id: int, created_at: datetime = None, updated_at: datetime = None):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.role_id = role_id
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at

    def update_password(self, new_password: str):
        """Updates the user's password."""
        self.password = new_password
        self.updated_at = datetime.now()

    def __str__(self):
        return f"User({self.first_name} {self.last_name}, Role ID: {self.role_id})"
