from abc import ABC, abstractmethod

class IAppointmentRepository(ABC):
    """Interfaz que define métodos específicos para la gestión de citas médicas."""

    @abstractmethod
    def get_appointments_by_doctor(self, doctor_id: int):
        """Obtiene todas las citas de un doctor específico."""
        pass

    @abstractmethod
    def get_appointments_by_patient(self, patient_id: int):
        """Obtiene todas las citas de un paciente específico."""
        pass

    @abstractmethod
    def get_upcoming_appointments(self):
        """Obtiene todas las citas futuras."""
        pass


class IDoctorRepository(ABC):
    """Interfaz que define métodos específicos para la gestión de doctores."""

    @abstractmethod
    def get_doctors_by_specialty(self, specialty_id: int):
        """Obtiene doctores por su especialidad."""
        pass

    @abstractmethod
    def get_availability(self, doctor_id: int):
        """Obtiene la disponibilidad de un doctor."""
        pass
