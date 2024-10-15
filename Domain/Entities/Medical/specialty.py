from datetime import datetime
from typing import Optional

class Specialty:
    def __init__(self, specialty_id: int, name: str):
        self.specialty_id = specialty_id
        self.name = name
        self.created_at = datetime.now()
        self.updated_at: Optional[datetime] = None
        self.is_active = True
    
    def deactivate_specialty(self):
        """Desactiva la especialidad médica"""
        self.is_active = False
        self.updated_at = datetime.now()

    def __repr__(self):
        return f"<Specialty {self.specialty_id}: {self.name}>"
