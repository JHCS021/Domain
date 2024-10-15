from datetime import datetime

class Notification:
    """
    Representa una notificación en el sistema.
    Sigue el principio de SRP: Esta clase solo se encarga de representar la información de una notificación.
    """
    def __init__(self, notification_id: int, user_id: int, message: str, sent_at: datetime = None):
        self.notification_id = notification_id  # Identificador único de la notificación
        self.user_id = user_id                  # ID del usuario que recibirá la notificación
        self.message = message                  # Mensaje de la notificación
        self.sent_at = sent_at or datetime.now() # Fecha y hora en que fue enviada (por defecto, ahora)

    def send(self):
        """
        Método para simular el envío de una notificación.
        En un futuro, este método se conectaría con un servicio de notificaciones.
        """
        print(f"Enviando notificación a usuario {self.user_id}: {self.message}")
        self.sent_at = datetime.now()

    def __str__(self):
        return f"Notification({self.notification_id}, User: {self.user_id}, Sent at: {self.sent_at})"
