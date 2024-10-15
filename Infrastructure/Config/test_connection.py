# test_connection.py
from sqlalchemy import create_engine
from database_config import DatabaseConfig

# Crear una instancia de la configuración de la base de datos
db_config = DatabaseConfig()

# Obtener la cadena de conexión
connection_string = db_config.get_connection_string()

# Probar la conexión a la base de datos
try:
    engine = create_engine(connection_string)
    connection = engine.connect()
    print("Conexión exitosa a la base de datos.")
    connection.close()
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")
