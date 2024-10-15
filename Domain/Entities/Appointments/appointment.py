from datetime import datetime

class Appointment:
    def __init__(self, appointment_id: int, patient_id: int, doctor_id: int, appointment_date: datetime, status_id: int):
        self.__appointment_id = appointment_id
        self.__patient_id = patient_id
        self.__doctor_id = doctor_id
        self.__appointment_date = appointment_date
        self.__status_id = status_id
        self.__created_at = datetime.now()
        self.__updated_at = None

    @property
    def appointment_id(self):
        return self.__appointment_id

    @property
    def patient_id(self):
        return self.__patient_id

    @property
    def doctor_id(self):
        return self.__doctor_id

    @property
    def appointment_date(self):
        return self.__appointment_date

    @appointment_date.setter
    def appointment_date(self, value: datetime):
        self.__appointment_date = value
        self.__set_updated_at()

    @property
    def status_id(self):
        return self.__status_id

    @status_id.setter
    def status_id(self, value: int):
        self.__status_id = value
        self.__set_updated_at()

    @property
    def created_at(self):
        return self.__created_at

    @property
    def updated_at(self):
        return self.__updated_at

    def __set_updated_at(self):
        """Sets the updated_at timestamp when a field is modified."""
        self.__updated_at = datetime.now()

    def reschedule(self, new_date: datetime):
        """Method to reschedule the appointment to a new date."""
        self.__appointment_date = new_date
        self.__set_updated_at()

    def cancel(self):
        """Method to cancel the appointment."""
        self.__status_id = 3  # Assume '3' means 'Cancelled'
        self.__set_updated_at()
