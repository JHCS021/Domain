from datetime import datetime
from .employee import Employee

class Nurse(Employee):
    def __init__(self, first_name: str, last_name: str, email: str, role_id: int, hire_date: datetime, 
                 license_number: str):
        super().__init__(first_name, last_name, email, role_id, hire_date)
        self.license_number = license_number

    def get_full_name(self):
        return f"Nurse {self.first_name} {self.last_name}"

    def get_license_info(self):
        return f"License Number: {self.license_number}"

    def __str__(self):
        return f"{self.get_full_name()} - License: {self.license_number}, Email: {self.email}"
