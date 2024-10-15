from base_repository import BaseRepository

class EmployeeRepository(BaseRepository):
    
    def __init__(self, db_context):
        self.db_context = db_context
    
    def get_by_id(self, employee_id: int):
        query = "SELECT * FROM Employees WHERE EmployeeID = ?"
        return self.db_context.execute(query, (employee_id,))

    def get_all(self):
        query = "SELECT * FROM Employees"
        return self.db_context.execute(query)

    def create(self, employee):
        query = """
        INSERT INTO Employees (FirstName, LastName, Email, RoleID, HireDate, CreatedAt)
        VALUES (?, ?, ?, ?, ?, GETDATE())
        """
        self.db_context.execute(query, (employee.FirstName, employee.LastName, employee.Email, 
                                        employee.RoleID, employee.HireDate))

    def update(self, employee):
        query = """
        UPDATE Employees 
        SET FirstName = ?, LastName = ?, Email = ?, RoleID = ?, HireDate = ?, UpdatedAt = GETDATE()
        WHERE EmployeeID = ?
        """
        self.db_context.execute(query, (employee.FirstName, employee.LastName, employee.Email, 
                                        employee.RoleID, employee.HireDate, employee.EmployeeID))

    def delete(self, employee_id: int):
        query = "DELETE FROM Employees WHERE EmployeeID = ?"
        self.db_context.execute(query, (employee_id,))
