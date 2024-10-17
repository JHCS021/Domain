class Patient:
    def __init__(self, patient_id, date_of_birth, gender, phone_number, address, blood_type, allergies, created_at=None, updated_at=None):
        self.patient_id = patient_id
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.phone_number = phone_number
        self.address = address
        self.blood_type = blood_type
        self.allergies = allergies
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        """Convierte el objeto a un diccionario para facilitar la persistencia"""
        return {
            "patient_id": self.patient_id,
            "date_of_birth": self.date_of_birth,
            "gender": self.gender,
            "phone_number": self.phone_number,
            "address": self.address,
            "blood_type": self.blood_type,
            "allergies": self.allergies,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
