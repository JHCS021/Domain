from abc import ABC, abstractmethod
from datetime import datetime

class Employee(ABC):
    def __init__(self, first_name: str, last_name: str, email: str, role_id: int, hire_date: datetime):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.role_id = role_id
        self.hire_date = hire_date
        self.created_at = datetime.now()
        self.updated_at = None

    @abstractmethod
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    @abstractmethod
    def get_contact_info(self):
        return f"Email: {self.email}"

    def update_contact_info(self, email: str):
        """Actualiza la información de contacto del empleado"""
        self.email = email
        self.updated_at = datetime.now()

    def __str__(self):
        return f"{self.get_full_name()} - {self.email}"
