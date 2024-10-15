from base_repository import BaseRepository

class AppointmentRepository(BaseRepository):
    
    def __init__(self, db_context):
        self.db_context = db_context
    
    def get_by_id(self, appointment_id: int):
        # SQL query to get an appointment by ID
        query = "SELECT * FROM Appointments WHERE AppointmentID = ?"
        return self.db_context.execute(query, (appointment_id,))

    def get_all(self):
        # SQL query to get all appointments
        query = "SELECT * FROM Appointments"
        return self.db_context.execute(query)

    def create(self, appointment):
        # SQL insert query for a new appointment
        query = """
        INSERT INTO Appointments (PatientID, DoctorID, AppointmentDate, StatusID, CreatedAt)
        VALUES (?, ?, ?, ?, GETDATE())
        """
        self.db_context.execute(query, (appointment.PatientID, appointment.DoctorID, 
                                        appointment.AppointmentDate, appointment.StatusID))

    def update(self, appointment):
        # SQL update query for an existing appointment
        query = """
        UPDATE Appointments 
        SET PatientID = ?, DoctorID = ?, AppointmentDate = ?, StatusID = ?, UpdatedAt = GETDATE() 
        WHERE AppointmentID = ?
        """
        self.db_context.execute(query, (appointment.PatientID, appointment.DoctorID, 
                                        appointment.AppointmentDate, appointment.StatusID, 
                                        appointment.AppointmentID))

    def delete(self, appointment_id: int):
        # SQL delete query for an appointment
        query = "DELETE FROM Appointments WHERE AppointmentID = ?"
        self.db_context.execute(query, (appointment_id,))
