# password_hasher.py
import bcrypt

class PasswordHasher:
    def hash_password(self, password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode(), salt)
        return hashed_password

    def verify_password(self, password, hashed_password):
        return bcrypt.checkpw(password.encode(), hashed_password)
