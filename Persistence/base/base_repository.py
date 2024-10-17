class BaseRepository:
    def __init__(self, db_context):
        self.db_context = db_context

    def get_by_id(self, table, entity_id):
        query = f"SELECT * FROM {table} WHERE ID = ?"
        with self.db_context as cursor:
            cursor.execute(query, (entity_id,))
            return cursor.fetchone()

    def create(self, table, columns, values):
        columns_str = ", ".join(columns)
        placeholders = ", ".join("?" for _ in values)
        query = f"INSERT INTO {table} ({columns_str}) VALUES ({placeholders})"
        with self.db_context as cursor:
            cursor.execute(query, values)
            cursor.commit()

    def update(self, table, entity_id, columns, values):
        set_clause = ", ".join(f"{col} = ?" for col in columns)
        query = f"UPDATE {table} SET {set_clause} WHERE ID = ?"
        with self.db_context as cursor:
            cursor.execute(query, (*values, entity_id))
            cursor.commit()

    def delete(self, table, entity_id):
        query = f"DELETE FROM {table} WHERE ID = ?"
        with self.db_context as cursor:
            cursor.execute(query, (entity_id,))
            cursor.commit()
