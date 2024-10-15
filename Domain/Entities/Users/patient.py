# domain/entities/users/patient.py

from datetime import datetime
from .user import User

class Patient(User):
    def __init__(self, user_id: int, first_name: str, last_name: str, email: str, password: str, role_id: int, date_of_birth: datetime, gender: str, phone_number: str, address: str, blood_type: str, allergies: str, insurance_provider_id: int, emergency_contact_name: str, emergency_contact_phone: str, created_at: datetime = None, updated_at: datetime = None):
        super().__init__(user_id, first_name, last_name, email, password, role_id, created_at, updated_at)
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.phone_number = phone_number
        self.address = address
        self.blood_type = blood_type
        self.allergies = allergies
        self.insurance_provider_id = insurance_provider_id
        self.emergency_contact_name = emergency_contact_name
        self.emergency_contact_phone = emergency_contact_phone

    def update_allergies(self, new_allergies: str):
        """Updates the patient's allergies."""
        self.allergies = new_allergies
        self.updated_at = datetime.now()

    def __str__(self):
        return f"Patient({self.first_name} {self.last_name}, Blood Type: {self.blood_type})"
