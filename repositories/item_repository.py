from sqlite3 import Connection, connect
from pydantic import BaseModel


class Item(BaseModel):
    id: int
    title: str
    equipment_id: int

class ItemRepository:
    def __init__(self, connection: Connection):
        self.connection = connection

    def create(self, title: str, equipment_id: int | None = None):
        sql = "INSERT INTO items (title, equipment_id) VALUES (?, ?)"
        cursor = self.connection.cursor()
        cursor.execute(sql, (title, equipment_id,))
        self.connection.commit()