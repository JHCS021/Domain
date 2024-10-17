class Appointment:
    def __init__(self, appointment_id, patient_id, doctor_id, appointment_date, status_id, created_at=None, updated_at=None):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_date = appointment_date
        self.status_id = status_id
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        """Convierte el objeto a un diccionario para facilitar la persistencia"""
        return {
            "appointment_id": self.appointment_id,
            "patient_id": self.patient_id,
            "doctor_id": self.doctor_id,
            "appointment_date": self.appointment_date,
            "status_id": self.status_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
