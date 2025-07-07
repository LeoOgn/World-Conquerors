from sqlite3 import Connection, connect
from typing import List


class LocationRepository:
    def __init__(self, connection: Connection):
        self.connection = connection

    def create(self, title: str, level_from: str, level_to: int):
        sql = "INSERT INTO locations (title, level_from, level_to) VALUES (?, ?, ?)"
        cursor = self.connection.cursor()
        cursor.execute(sql, (title, level_from, level_to))
        self.connection.commit()

    def get_all(self) -> List[tuple]:
        sql = "SELECT * FROM locations"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        return cursor.fetchall()