from dataclasses import dataclass

@dataclass(frozen=True)
class Address:
    street: str
    city: str
    state: str
    postal_code: str
    country: str

    def __post_init__(self):
        if not self.postal_code.isdigit():
            raise ValueError("Postal code must be numeric.")

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.postal_code}, {self.country}"

    def is_valid(self) -> bool:
        # Validación simple, puede expandirse
        return all([self.street, self.city, self.state, self.postal_code, self.country])
