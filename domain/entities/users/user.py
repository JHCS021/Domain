# domain/entities/users/user.py

from domain.entities.base_entity import BaseEntity

class User(BaseEntity):
    def __init__(self, name: str, email: str, phone: str, role: str, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        self.phone = phone
        self.role = role  # Puede ser 'doctor' o 'paciente'
