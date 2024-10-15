from abc import ABC, abstractmethod

class BaseRepository(ABC):
    """Interfaz base para repositorios que define las operaciones CRUD."""
    
    @abstractmethod
    def create(self, entity):
        """Crea una nueva entidad en el repositorio."""
        pass

    @abstractmethod
    def update(self, entity):
        """Actualiza una entidad existente en el repositorio."""
        pass

    @abstractmethod
    def delete(self, entity_id: int):
        """Elimina una entidad del repositorio por su ID."""
        pass

    @abstractmethod
    def get_by_id(self, entity_id: int):
        """Obtiene una entidad por su ID."""
        pass

    @abstractmethod
    def get_all(self):
        """Obtiene todas las entidades del repositorio."""
        pass
