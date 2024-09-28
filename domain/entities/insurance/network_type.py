# domain/entities/insurance/network_type.py

from domain.entities.base_entity import BaseEntity

class NetworkType(BaseEntity):
    def __init__(self, name: str, description: str = "", **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
