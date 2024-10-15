from base_repository import BaseRepository

class DoctorRepository(BaseRepository):
    
    def __init__(self, db_context):
        self.db_context = db_context
    
    def get_by_id(self, doctor_id: int):
        # SQL query to get a doctor by ID
        query = "SELECT * FROM Doctors WHERE DoctorID = ?"
        return self.db_context.execute(query, (doctor_id,))

    def get_all(self):
        # SQL query to get all doctors
        query = "SELECT * FROM Doctors"
        return self.db_context.execute(query)

    def create(self, doctor):
        # SQL insert query for a new doctor
        query = """
        INSERT INTO Doctors (SpecialtyID, LicenseNumber, PhoneNumber, YearsOfExperience, Bio, ConsultationFee, CreatedAt)
        VALUES (?, ?, ?, ?, ?, ?, GETDATE())
        """
        self.db_context.execute(query, (doctor.SpecialtyID, doctor.LicenseNumber, 
                                        doctor.PhoneNumber, doctor.YearsOfExperience, 
                                        doctor.Bio, doctor.ConsultationFee))

    def update(self, doctor):
        # SQL update query for an existing doctor
        query = """
        UPDATE Doctors 
        SET SpecialtyID = ?, LicenseNumber = ?, PhoneNumber = ?, YearsOfExperience = ?, Bio = ?, ConsultationFee = ?, UpdatedAt = GETDATE() 
        WHERE DoctorID = ?
        """
        self.db_context.execute(query, (doctor.SpecialtyID, doctor.LicenseNumber, 
                                        doctor.PhoneNumber, doctor.YearsOfExperience, 
                                        doctor.Bio, doctor.ConsultationFee, 
                                        doctor.DoctorID))

    def delete(self, doctor_id: int):
        # SQL delete query for a doctor
        query = "DELETE FROM Doctors WHERE DoctorID = ?"
        self.db_context.execute(query, (doctor_id,))
