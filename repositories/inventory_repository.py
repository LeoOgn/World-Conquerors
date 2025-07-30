from sqlite3 import Connection, connect
from pydantic import BaseModel

class Inventory(BaseModel):
    ...


class InventoryRepository:
    def __init__(self, connection: Connection):
        self.connection = connection

    def add_item(self, character_id: int, item_id: int):
        sql = "INSERT INTO inventory (character_id, item_id) VALUES (?, ?)"
        cursor = self.connection.cursor()
        cursor.execute(sql, (character_id, item_id,))
        self.connection.commit()
