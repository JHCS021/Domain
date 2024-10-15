from datetime import datetime

class BaseEntity:
    """Clase base para todas las entidades del sistema, proporcionando
    atributos y métodos comunes como ID y timestamps."""
    
    def __init__(self, id: int = None, created_at: datetime = None, updated_at: datetime = None):
        self.id = id
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

    def update_timestamp(self):
        """Actualiza el timestamp de la entidad cuando se realiza alguna modificación."""
        self.updated_at = datetime.now()

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id})"
