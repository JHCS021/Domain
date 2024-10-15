from dataclasses import dataclass
from .email import Email
from .phone_number import PhoneNumber

@dataclass(frozen=True)
class ContactInfo:
    email: Email
    phone_number: PhoneNumber

    def __str__(self):
        return f"Email: {self.email}, Phone: {self.phone_number}"

    def is_valid(self) -> bool:
        return self.email.is_valid() and self.phone_number.is_valid()
