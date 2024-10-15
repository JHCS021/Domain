from abc import ABC, abstractmethod

class IEmailService(ABC):
    @abstractmethod
    def send_email(self, to: str, subject: str, message: str) -> bool:
        """Send an email to a recipient"""
        pass

class SMTPEmailService(IEmailService):
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, to: str, subject: str, message: str) -> bool:
        try:
            # Aquí se implementa la lógica para enviar correo vía SMTP
            print(f"Enviando correo a {to}: {subject}")
            return True  # Simula que el correo fue enviado
        except Exception as e:
            print(f"Error enviando correo: {e}")
            return False
