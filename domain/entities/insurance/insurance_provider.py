# domain/entities/insurance/insurance_provider.py

from domain.entities.base_entity import BaseEntity

class InsuranceProvider(BaseEntity):
    def __init__(self, name: str, contact_number: str, email: str, address: str, coverage_details: str, is_preferred: bool, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.contact_number = contact_number
        self.email = email
        self.address = address
        self.coverage_details = coverage_details
        self.is_preferred = is_preferred
