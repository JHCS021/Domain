from .data_access_exception import DataAccessException

class DatabaseConnectionException(DataAccessException):
    """Excepción lanzada cuando ocurre un problema de conexión a la base de datos."""
    def __init__(self, server_name):
        message = f"No se pudo conectar al servidor de base de datos: {server_name}"
        super().__init__(message)
