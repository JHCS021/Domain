class DataAccessException(Exception):
    """Excepción base para todos los errores relacionados con el acceso a datos."""
    def __init__(self, message="Error en el acceso a los datos", original_exception=None):
        super().__init__(message)
        self.original_exception = original_exception
