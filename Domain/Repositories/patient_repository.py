from base_repository import BaseRepository

class PatientRepository(BaseRepository):
    
    def __init__(self, db_context):
        self.db_context = db_context
    
    def get_by_id(self, patient_id: int):
        # SQL query to get a patient by ID
        query = "SELECT * FROM Patients WHERE PatientID = ?"
        return self.db_context.execute(query, (patient_id,))

    def get_all(self):
        # SQL query to get all patients
        query = "SELECT * FROM Patients"
        return self.db_context.execute(query)

    def create(self, patient):
        # SQL insert query for a new patient
        query = """
        INSERT INTO Patients (DateOfBirth, Gender, PhoneNumber, Address, BloodType, Allergies, InsuranceProviderID, EmergencyContactName, EmergencyContactPhone, CreatedAt)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, GETDATE())
        """
        self.db_context.execute(query, (patient.DateOfBirth, patient.Gender, patient.PhoneNumber, 
                                        patient.Address, patient.BloodType, patient.Allergies, 
                                        patient.InsuranceProviderID, patient.EmergencyContactName, 
                                        patient.EmergencyContactPhone))

    def update(self, patient):
        # SQL update query for an existing patient
        query = """
        UPDATE Patients 
        SET DateOfBirth = ?, Gender = ?, PhoneNumber = ?, Address = ?, BloodType = ?, Allergies = ?, InsuranceProviderID = ?, EmergencyContactName = ?, EmergencyContactPhone = ?, UpdatedAt = GETDATE()
        WHERE PatientID = ?
        """
        self.db_context.execute(query, (patient.DateOfBirth, patient.Gender, patient.PhoneNumber, 
                                        patient.Address, patient.BloodType, patient.Allergies, 
                                        patient.InsuranceProviderID, patient.EmergencyContactName, 
                                        patient.EmergencyContactPhone, patient.PatientID))

    def delete(self, patient_id: int):
        # SQL delete query for a patient
        query = "DELETE FROM Patients WHERE PatientID = ?"
        self.db_context.execute(query, (patient_id,))
