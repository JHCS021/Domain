from datetime import datetime
from .employee import Employee

class Doctor(Employee):
    def __init__(self, first_name: str, last_name: str, email: str, role_id: int, hire_date: datetime, 
                 license_number: str, specialty_id: int, years_of_experience: int):
        super().__init__(first_name, last_name, email, role_id, hire_date)
        self.license_number = license_number
        self.specialty_id = specialty_id
        self.years_of_experience = years_of_experience
        self.bio = None

    def get_full_name(self):
        return f"Dr. {self.first_name} {self.last_name}"

    def set_bio(self, bio: str):
        """Define la biografía del doctor"""
        self.bio = bio
        self.updated_at = datetime.now()

    def get_specialty_info(self):
        return f"Specialty ID: {self.specialty_id}, License: {self.license_number}"

    def __str__(self):
        return f"{self.get_full_name()} - {self.email}, Specialty ID: {self.specialty_id}"
