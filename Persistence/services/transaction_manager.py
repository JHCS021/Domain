class TransactionManager:
    def __init__(self, db_context):
        self.db_context = db_context
        self.transaction = None

    def begin_transaction(self):
        """
        Inicia una transacción en la base de datos.
        """
        self.transaction = self.db_context.connection.cursor()
        self.transaction.execute('BEGIN TRANSACTION')

    def commit(self):
        """
        Confirma los cambios realizados durante la transacción.
        """
        try:
            self.transaction.connection.commit()
            self.transaction.close()
        except Exception as e:
            self.rollback()
            raise e

    def rollback(self):
        """
        Revierte los cambios realizados durante la transacción en caso de error.
        """
        if self.transaction:
            self.transaction.connection.rollback()
            self.transaction.close()

    def __enter__(self):
        self.begin_transaction()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.rollback()
        else:
            self.commit()
