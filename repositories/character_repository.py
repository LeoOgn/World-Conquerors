from sqlite3 import Connection, connect


class CharacterRepository:
    def __init__(self, connection: Connection):
        self.connection = connection

    def create(self, name: str, user_id: int):
        sql = "INSERT INTO characters (name, user_id) VALUES (?, ?)"
        cursor = self.connection.cursor()
        cursor.execute(sql, (name, user_id))
        self.connection.commit()

    