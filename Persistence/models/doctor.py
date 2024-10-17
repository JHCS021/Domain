class Doctor:
    def __init__(self, doctor_id, specialty_id, license_number, phone_number, years_of_experience, consultation_fee, created_at=None, updated_at=None):
        self.doctor_id = doctor_id
        self.specialty_id = specialty_id
        self.license_number = license_number
        self.phone_number = phone_number
        self.years_of_experience = years_of_experience
        self.consultation_fee = consultation_fee
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        """Convierte el objeto a un diccionario para facilitar la persistencia"""
        return {
            "doctor_id": self.doctor_id,
            "specialty_id": self.specialty_id,
            "license_number": self.license_number,
            "phone_number": self.phone_number,
            "years_of_experience": self.years_of_experience,
            "consultation_fee": self.consultation_fee,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
