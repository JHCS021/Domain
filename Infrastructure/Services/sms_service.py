from abc import ABC, abstractmethod

class ISMSService(ABC):
    @abstractmethod
    def send_sms(self, to: str, message: str) -> bool:
        """Send an SMS to a recipient"""
        pass

class TwilioSMSService(ISMSService):
    def __init__(self, account_sid: str, auth_token: str, from_number: str):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.from_number = from_number

    def send_sms(self, to: str, message: str) -> bool:
        try:
            # Aquí se implementa la lógica para enviar SMS usando Twilio API
            print(f"Enviando SMS a {to}: {message}")
            return True  # Simula que el SMS fue enviado
        except Exception as e:
            print(f"Error enviando SMS: {e}")
            return False
