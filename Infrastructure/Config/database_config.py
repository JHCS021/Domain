# database_config.py
import os

class DatabaseConfig:
    def __init__(self):
        self.database = os.getenv('DB_NAME', 'MedicalAppointment_DB')
        self.host = os.getenv('DB_HOST', 'JHCS25')  # Prueba con la IP o el nombre completo de la instancia
        self.port = os.getenv('DB_PORT', '1433')
        self.username = os.getenv('DB_USERNAME', 'tu_usuario')  # Usuario de SQL Server (si aplica)
        self.password = os.getenv('DB_PASSWORD', 'tu_contraseña')  # Contraseña de SQL Server (si aplica)

    def get_connection_string(self):
        """
        Devuelve la cadena de conexión utilizando pymssql.
        """
        return f"mssql+pymssql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"

# Ejemplo de uso
# db_config = DatabaseConfig()
# connection_string = db_config.get_connection_string()
# print(connection_string)  # Verificación de la cadena de conexión
