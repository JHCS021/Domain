class Notification:
    def __init__(self, notification_id, user_id, message, sent_at):
        self.notification_id = notification_id
        self.user_id = user_id
        self.message = message
        self.sent_at = sent_at

    def to_dict(self):
        """Convierte el objeto a un diccionario para facilitar la persistencia"""
        return {
            "notification_id": self.notification_id,
            "user_id": self.user_id,
            "message": self.message,
            "sent_at": self.sent_at
        }
