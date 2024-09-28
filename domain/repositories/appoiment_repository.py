# persistence/repositories/appointment_repository.py

from sqlalchemy.orm import Session
from domain.entities.appointments.appointment import Appointment
from domain.repositories.i_base_repository import IBaseRepository

class AppointmentRepository(IBaseRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, id: int):
        return self.session.query(Appointment).filter(Appointment.id == id).first()

    def add(self, entity: Appointment):
        self.session.add(entity)
        self.session.commit()

    def update(self, entity: Appointment):
        self.session.merge(entity)
        self.session.commit()

    def delete(self, id: int):
        entity = self.get_by_id(id)
        if entity:
            self.session.delete(entity)
            self.session.commit()
