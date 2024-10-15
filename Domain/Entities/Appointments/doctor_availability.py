from datetime import datetime, time

class DoctorAvailability:
    def __init__(self, availability_id: int, doctor_id: int, available_date: datetime, start_time: time, end_time: time):
        self.__availability_id = availability_id
        self.__doctor_id = doctor_id
        self.__available_date = available_date
        self.__start_time = start_time
        self.__end_time = end_time
        self.__created_at = datetime.now()

    @property
    def availability_id(self):
        return self.__availability_id

    @property
    def doctor_id(self):
        return self.__doctor_id

    @property
    def available_date(self):
        return self.__available_date

    @available_date.setter
    def available_date(self, value: datetime):
        self.__available_date = value

    @property
    def start_time(self):
        return self.__start_time

    @start_time.setter
    def start_time(self, value: time):
        self.__start_time = value

    @property
    def end_time(self):
        return self.__end_time

    @end_time.setter
    def end_time(self, value: time):
        self.__end_time = value

    @property
    def created_at(self):
        return self.__created_at

    def is_available(self, requested_date: datetime, requested_time: time) -> bool:
        """Checks if the doctor is available at the requested date and time."""
        return self.__available_date == requested_date and self.__start_time <= requested_time <= self.__end_time
