class Employee:
    def __init__(self, employee_id, first_name, last_name, email, role_id, hire_date, created_at=None, updated_at=None):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.role_id = role_id
        self.hire_date = hire_date
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        """Convierte el objeto a un diccionario para facilitar la persistencia"""
        return {
            "employee_id": self.employee_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "role_id": self.role_id,
            "hire_date": self.hire_date,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
