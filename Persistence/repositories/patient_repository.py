from .db_context import DBContext

class PatientRepository:
    def __init__(self, server_name, database_name, user=None, password=None):
        self.db_context = DBContext(server_name, database_name, user, password)

    def get_patient_by_name(self, first_name, last_name):
        query = "SELECT * FROM Users.Patient WHERE FirstName = %s AND LastName = %s"
        with self.db_context as cursor:
            cursor.execute(query, (first_name, last_name))
            return cursor.fetchone()
