from .db_context import DBContext
from ..exceptions.record_not_found_exception import RecordNotFoundException
from ..exceptions.database_connection_exception import DatabaseConnectionException

class AppointmentRepository:
    def __init__(self, server_name, database_name, user=None, password=None):
        self.db_context = DBContext(server_name, database_name, user, password)

    def get_appointments_by_doctor(self, doctor_id):
        query = "SELECT * FROM Appointments.Appointment WHERE DoctorID = %s"
        with self.db_context as cursor:
            cursor.execute(query, (doctor_id,))
            return cursor.fetchall()

    def create_appointment(self, patient_id, doctor_id, appointment_date, status_id):
        query = """INSERT INTO Appointments.Appointment (PatientID, DoctorID, AppointmentDate, StatusID)
                   VALUES (%s, %s, %s, %s)"""
        with self.db_context as cursor:
            cursor.execute(query, (patient_id, doctor_id, appointment_date, status_id))
            cursor.connection.commit()

    def get_appointment_by_id(self, appointment_id):
            try:
                query = "SELECT * FROM Appointments.Appointment WHERE AppointmentID = %s"
                with self.db_context as cursor:
                    cursor.execute(query, (appointment_id,))
                    result = cursor.fetchone()

                if not result:
                    raise RecordNotFoundException("Appointment", appointment_id)

                return result

            except DatabaseConnectionException as e:
                raise DatabaseConnectionException(self.db_context.server_name)