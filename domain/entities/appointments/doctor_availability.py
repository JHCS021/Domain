# domain/entities/appointments/doctor_availability.py

from domain.entities.base_entity import BaseEntity
from datetime import time, date

class DoctorAvailability(BaseEntity):
    def __init__(self, doctor_id: int, available_date: date, start_time: time, end_time: time, **kwargs):
        super().__init__(**kwargs)
        self.doctor_id = doctor_id
        self.available_date = available_date
        self.start_time = start_time
        self.end_time = end_time
