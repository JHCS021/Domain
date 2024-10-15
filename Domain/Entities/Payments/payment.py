
class Payment:
    def __init__(self, payment_id: int, patient_id: int, amount: float, method: str, 
                 status: str, created_at: str, updated_at: str = None):
        self.payment_id = payment_id
        self.patient_id = patient_id
        self.amount = amount
        self.method = method  # e.g., 'credit_card', 'paypal', etc.
        self.status = status  # e.g., 'completed', 'pending', 'failed'
        self.created_at = created_at
        self.updated_at = updated_at

    def process_payment(self):
        # Logic to process the payment
        pass

    def refund(self):
        # Logic to refund a payment
        pass

    def __repr__(self):
        return f"Payment(payment_id={self.payment_id}, patient_id={self.patient_id}, amount={self.amount})"
