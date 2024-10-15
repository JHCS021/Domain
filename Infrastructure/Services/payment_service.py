from abc import ABC, abstractmethod

class IPaymentService(ABC):
    @abstractmethod
    def process_payment(self, amount: float, currency: str, source: str, description: str) -> bool:
        """Process a payment"""
        pass

class StripePaymentService(IPaymentService):
    def __init__(self, api_key: str):
        self.api_key = api_key

    def process_payment(self, amount: float, currency: str, source: str, description: str) -> bool:
        try:
            # Aquí se implementa la lógica para procesar el pago con Stripe
            print(f"Procesando pago de {amount} {currency} con Stripe")
            return True  # Simula que el pago fue procesado
        except Exception as e:
            print(f"Error procesando el pago: {e}")
            return False
