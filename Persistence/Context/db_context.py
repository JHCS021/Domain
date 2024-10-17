import pymssql

class DBContext:
    def __init__(self, server_name, database_name, user=None, password=None):
        # Conexión utilizando pymssql
        self.server_name = server_name
        self.database_name = database_name
        self.user = user
        self.password = password
        self.connection = None

    def __enter__(self):
        # Abre la conexión con SQL Server
        if self.user and self.password:
            self.connection = pymssql.connect(
                server=self.server_name,
                user=self.user,
                password=self.password,
                database=self.database_name
            )
        else:
            # Conexión utilizando autenticación de Windows (si no se proporcionan usuario y contraseña)
            self.connection = pymssql.connect(server=self.server_name, database=self.database_name)
        return self.connection.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Cierra la conexión
        if self.connection:
            self.connection.close()
