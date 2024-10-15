# domain/entities/users/doctor.py

from datetime import datetime
from .user import User

class Doctor(User):
    def __init__(self, user_id: int, first_name: str, last_name: str, email: str, password: str, role_id: int, specialty_id: int, license_number: str, years_of_experience: int, bio: str = None, consultation_fee: float = None, created_at: datetime = None, updated_at: datetime = None):
        super().__init__(user_id, first_name, last_name, email, password, role_id, created_at, updated_at)
        self.specialty_id = specialty_id
        self.license_number = license_number
        self.years_of_experience = years_of_experience
        self.bio = bio
        self.consultation_fee = consultation_fee

    def update_specialty(self, new_specialty_id: int):
        """Updates the doctor's specialty."""
        self.specialty_id = new_specialty_id
        self.updated_at = datetime.now()

    def __str__(self):
        return f"Doctor({self.first_name} {self.last_name}, Specialty ID: {self.specialty_id}, Experience: {self.years_of_experience} years)"
