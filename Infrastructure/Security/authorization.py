# authorization.py
class AuthorizationService:
    def __init__(self, role_repository):
        self.role_repository = role_repository

    def is_authorized(self, user, required_role):
        user_role = self.role_repository.get_role_by_user_id(user.UserID)
        return user_role == required_role
