from base_repository import BaseRepository

class NotificationRepository(BaseRepository):
    
    def __init__(self, db_context):
        self.db_context = db_context
    
    def get_by_id(self, notification_id: int):
        # SQL query to get a notification by ID
        query = "SELECT * FROM System.Notification WHERE NotificationID = ?"
        return self.db_context.execute(query, (notification_id,))

    def get_all(self):
        # SQL query to get all notifications
        query = "SELECT * FROM System.Notification"
        return self.db_context.execute(query)

    def create(self, notification):
        # SQL insert query for a new notification
        query = """
        INSERT INTO System.Notification (UserID, Message, SentAt)
        VALUES (?, ?, GETDATE())
        """
        self.db_context.execute(query, (notification.UserID, notification.Message))

    def update(self, notification):
        # SQL update query for an existing notification
        query = """
        UPDATE System.Notification 
        SET UserID = ?, Message = ?, SentAt = GETDATE()
        WHERE NotificationID = ?
        """
        self.db_context.execute(query, (notification.UserID, notification.Message, notification.NotificationID))

    def delete(self, notification_id: int):
        # SQL delete query for a notification
        query = "DELETE FROM System.Notification WHERE NotificationID = ?"
        self.db_context.execute(query, (notification_id,))


class NotificationLogRepository(BaseRepository):
    
    def __init__(self, db_context):
        self.db_context = db_context

    def get_by_id(self, log_id: int):
        # SQL query to get a notification log by ID
        query = "SELECT * FROM System.NotificationLog WHERE LogID = ?"
        return self.db_context.execute(query, (log_id,))

    def get_all(self):
        # SQL query to get all notification logs
        query = "SELECT * FROM System.NotificationLog"
        return self.db_context.execute(query)

    def create(self, log):
        # SQL insert query for a new notification log
        query = """
        INSERT INTO System.NotificationLog (NotificationID, SentAt, Status)
        VALUES (?, GETDATE(), ?)
        """
        self.db_context.execute(query, (log.NotificationID, log.Status))

    def update(self, log):
        # SQL update query for an existing notification log
        query = """
        UPDATE System.NotificationLog 
        SET NotificationID = ?, SentAt = GETDATE(), Status = ?
        WHERE LogID = ?
        """
        self.db_context.execute(query, (log.NotificationID, log.Status, log.LogID))

    def delete(self, log_id: int):
        # SQL delete query for a notification log
        query = "DELETE FROM System.NotificationLog WHERE LogID = ?"
        self.db_context.execute(query, (log_id,))
