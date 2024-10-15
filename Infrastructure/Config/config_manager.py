# config_manager.py
from Infrastructure.Config.database_config import DatabaseConfig

class ConfigManager:
    """
    Clase responsable de centralizar la configuración de la aplicación.
    Puede gestionar múltiples tipos de configuración (BD, servicios externos, etc.).
    """
    def __init__(self):
        self.database_config = DatabaseConfig()

    def get_database_connection_string(self):
        """
        Devuelve la cadena de conexión de la base de datos.
        """
        return self.database_config.get_connection_string()

# Ejemplo de uso
# config_manager = ConfigManager()
# db_connection_string = config_manager.get_database_connection_string()
# print(db_connection_string)
