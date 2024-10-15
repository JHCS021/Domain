from dataclasses import dataclass
import re

@dataclass(frozen=True)
class PhoneNumber:
    value: str

    def __post_init__(self):
        if not self.is_valid():
            raise ValueError(f"Invalid phone number format: {self.value}")

    def is_valid(self) -> bool:
        # Simple regex for phone number validation
        pattern = r"^\+?\d{10,15}$"  # Ejemplo: +1234567890 o 1234567890
        return re.match(pattern, self.value) is not None

    def __str__(self):
        return self.value
