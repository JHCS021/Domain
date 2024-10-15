class AppointmentStatus:
    def __init__(self, status_id: int, status_name: str):
        self.__status_id = status_id
        self.__status_name = status_name

    @property
    def status_id(self):
        return self.__status_id

    @property
    def status_name(self):
        return self.__status_name

    def __str__(self):
        return f"Status: {self.__status_name} (ID: {self.__status_id})"
