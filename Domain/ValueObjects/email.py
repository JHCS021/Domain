from dataclasses import dataclass
import re

@dataclass(frozen=True)
class Email:
    value: str

    def __post_init__(self):
        if not self.is_valid():
            raise ValueError(f"Invalid email format: {self.value}")

    def is_valid(self) -> bool:
        pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        return re.match(pattern, self.value) is not None

    def __str__(self):
        return self.value
