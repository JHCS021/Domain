# domain/entities/appointments/appointment.py

from domain.entities.base_entity import BaseEntity
from datetime import datetime

class Appointment(BaseEntity):
    def __init__(self, patient_id: int, doctor_id: int, appointment_date: datetime, status_id: int, **kwargs):
        super().__init__(**kwargs)
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_date = appointment_date
        self.status_id = status_id
        self.created_at = datetime.now()
        self.updated_at = None
