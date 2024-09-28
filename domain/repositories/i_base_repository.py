# domain/repositories/i_base_repository.py

from abc import ABC, abstractmethod

class IBaseRepository(ABC):
    @abstractmethod
    def get_by_id(self, id: int):
        pass

    @abstractmethod
    def add(self, entity):
        pass

    @abstractmethod
    def update(self, entity):
        pass

    @abstractmethod
    def delete(self, id: int):
        pass
