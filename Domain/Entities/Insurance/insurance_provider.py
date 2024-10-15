# insurance_provider.py
from datetime import datetime
from typing import Optional


class InsuranceProvider:
    def __init__(self, name: str, contact_number: str, email: str, address: str, 
                 website: Optional[str] = None, created_at: Optional[datetime] = None):
        self.name = name
        self.contact_number = contact_number
        self.email = email
        self.address = address
        self.website = website
        self.created_at = created_at or datetime.now()
        self.updated_at = None  # To be updated later

    def update_contact_info(self, contact_number: str, email: str, address: str, website: Optional[str] = None):
        """Update contact information of the insurance provider."""
        self.contact_number = contact_number
        self.email = email
        self.address = address
        self.website = website
        self.updated_at = datetime.now()

    def __str__(self):
        return f"InsuranceProvider(name={self.name}, contact_number={self.contact_number})"
