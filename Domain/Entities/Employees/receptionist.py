from datetime import datetime
from .employee import Employee

class Receptionist(Employee):
    def __init__(self, first_name: str, last_name: str, email: str, role_id: int, hire_date: datetime, shift: str):
        super().__init__(first_name, last_name, email, role_id, hire_date)
        self.shift = shift

    def get_full_name(self):
        return f"Receptionist {self.first_name} {self.last_name}"

    def get_shift_info(self):
        return f"Shift: {self.shift}"

    def __str__(self):
        return f"{self.get_full_name()} - {self.email}, Shift: {self.shift}"
