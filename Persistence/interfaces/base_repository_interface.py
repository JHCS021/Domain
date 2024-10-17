from abc import ABC, abstractmethod

class IBaseRepository(ABC):
    """Interfaz base que define las operaciones CRUD genéricas."""

    @abstractmethod
    def get_by_id(self, entity_id: int):
        """Recupera una entidad por su ID."""
        pass

    @abstractmethod
    def get_all(self):
        """Recupera todas las entidades."""
        pass

    @abstractmethod
    def create(self, entity):
        """Crea una nueva entidad."""
        pass

    @abstractmethod
    def update(self, entity_id: int, entity):
        """Actualiza una entidad existente por su ID."""
        pass

    @abstractmethod
    def delete(self, entity_id: int):
        """Elimina una entidad por su ID."""
        pass
