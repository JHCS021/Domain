from datetime import datetime
from typing import Optional

class Prescription:
    def __init__(self, prescription_id: int, medical_record_id: int, medication: str, dosage: str, frequency: str, duration: str):
        self.prescription_id = prescription_id
        self.medical_record_id = medical_record_id
        self.medication = medication
        self.dosage = dosage
        self.frequency = frequency
        self.duration = duration
        self.created_at = datetime.now()

    def update_prescription(self, new_medication: str, new_dosage: str, new_frequency: str, new_duration: str):
        """Permite actualizar los detalles de una prescripción"""
        self.medication = new_medication
        self.dosage = new_dosage
        self.frequency = new_frequency
        self.duration = new_duration

    def __repr__(self):
        return f"<Prescription {self.prescription_id}: {self.medication} - {self.dosage}>"
