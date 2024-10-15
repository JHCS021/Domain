# authentication.py
from password_hasher import PasswordHasher

class AuthenticationService:
    def __init__(self, user_repository):
        self.user_repository = user_repository
        self.password_hasher = PasswordHasher()

    def login(self, email, password):
        user = self.user_repository.get_user_by_email(email)
        if user and self.password_hasher.verify_password(password, user.password):
            # Generate token or session, etc.
            return self.generate_token(user)
        return None

    def generate_token(self, user):
        # Aquí puedes usar JWT o cualquier otro sistema de tokens.
        token = f"token_for_{user.UserID}"  # Ejemplo básico
        return token
