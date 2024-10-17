from .db_context import DBContext

class EmployeeRepository:
    def __init__(self, server_name, database_name, user=None, password=None):
        self.db_context = DBContext(server_name, database_name, user, password)

    def get_employee_by_role(self, role_id):
        query = "SELECT * FROM Employees.Employee WHERE RoleID = %s"
        with self.db_context as cursor:
            cursor.execute(query, (role_id,))
            return cursor.fetchall()
