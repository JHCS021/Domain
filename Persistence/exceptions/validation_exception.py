from .data_access_exception import DataAccessException

class ValidationException(DataAccessException):
    """Excepción lanzada cuando los datos no cumplen con los criterios de validación."""
    def __init__(self, validation_errors):
        message = "Los datos no son válidos: " + ", ".join(validation_errors)
        super().__init__(message)
        self.validation_errors = validation_errors
