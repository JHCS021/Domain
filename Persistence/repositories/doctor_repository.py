from .db_context import DBContext

class DoctorRepository:
    def __init__(self, server_name, database_name, user=None, password=None):
        self.db_context = DBContext(server_name, database_name, user, password)

    def get_doctors_by_specialty(self, specialty_id):
        query = "SELECT * FROM Users.Doctor WHERE SpecialtyID = %s"
        with self.db_context as cursor:
            cursor.execute(query, (specialty_id,))
            return cursor.fetchall()

    def get_availability(self, doctor_id):
        query = "SELECT * FROM Appointments.DoctorAvailability WHERE DoctorID = %s"
        with self.db_context as cursor:
            cursor.execute(query, (doctor_id,))
            return cursor.fetchall()
