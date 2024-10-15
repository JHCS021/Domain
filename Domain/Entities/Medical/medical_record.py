from datetime import datetime
from typing import Optional

class MedicalRecord:
    def __init__(self, record_id: int, patient_id: int, doctor_id: int, diagnosis: str, treatment: str, date_of_visit: datetime):
        self.record_id = record_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.diagnosis = diagnosis
        self.treatment = treatment
        self.date_of_visit = date_of_visit
        self.created_at = datetime.now()
        self.updated_at: Optional[datetime] = None

    def update_treatment(self, new_treatment: str):
        """Permite actualizar el tratamiento de un registro médico"""
        self.treatment = new_treatment
        self.updated_at = datetime.now()
    
    def update_diagnosis(self, new_diagnosis: str):
        """Permite actualizar el diagnóstico de un registro médico"""
        self.diagnosis = new_diagnosis
        self.updated_at = datetime.now()
    
    def __repr__(self):
        return f"<MedicalRecord {self.record_id}: {self.diagnosis}>"
