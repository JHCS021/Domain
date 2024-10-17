from .data_access_exception import DataAccessException

class RecordNotFoundException(DataAccessException):
    """Excepción lanzada cuando no se encuentra un registro en la base de datos."""
    def __init__(self, entity_name, record_id):
        message = f"El registro de {entity_name} con ID {record_id} no fue encontrado."
        super().__init__(message)
