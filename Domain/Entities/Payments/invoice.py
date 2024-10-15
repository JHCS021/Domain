
class Invoice:
    def __init__(self, invoice_id: int, patient_id: int, total_amount: float, 
                 is_paid: bool, created_at: str, updated_at: str = None):
        self.invoice_id = invoice_id
        self.patient_id = patient_id
        self.total_amount = total_amount
        self.is_paid = is_paid
        self.created_at = created_at
        self.updated_at = updated_at

    def mark_as_paid(self):
        self.is_paid = True
        # Logic to handle post-payment actions, such as updating payment status
        pass

    def calculate_total(self, items):
        # Logic to calculate total from a list of items (services, products)
        self.total_amount = sum(item['price'] for item in items)
        pass

    def __repr__(self):
        return f"Invoice(invoice_id={self.invoice_id}, patient_id={self.patient_id}, total_amount={self.total_amount}, is_paid={self.is_paid})"
