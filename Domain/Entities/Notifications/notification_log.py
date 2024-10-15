from datetime import datetime

class NotificationLog:
    """
    Registra el historial de notificaciones enviadas.
    Esta clase sigue el principio de SRP, solo se encarga de representar un log de notificación.
    """
    def __init__(self, log_id: int, notification_id: int, status: str, sent_at: datetime = None):
        self.log_id = log_id                    # ID único del log
        self.notification_id = notification_id  # Referencia a la notificación
        self.status = status                    # Estado del envío (Enviado, Fallido, etc.)
        self.sent_at = sent_at or datetime.now() # Fecha y hora del log

    def __str__(self):
        return f"NotificationLog(LogID: {self.log_id}, NotificationID: {self.notification_id}, Status: {self.status}, Sent at: {self.sent_at})"
