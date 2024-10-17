from .db_context import DBContext

class NotificationRepository:
    def __init__(self, server_name, database_name, user=None, password=None):
        self.db_context = DBContext(server_name, database_name, user, password)

    def log_notification(self, notification_id, status):
        query = "INSERT INTO System.NotificationLog (NotificationID, Status) VALUES (%s, %s)"
        with self.db_context as cursor:
            cursor.execute(query, (notification_id, status))
            cursor.connection.commit()
