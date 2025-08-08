from sqlite3 import Connection, connect
from pydantic import BaseModel
from repositories import Equipment


class Item(BaseModel):
    id: int
    title: str
    equipment_id: int | None = None
    
class ItemRepository:
    def __init__(self, connection: Connection):
        self.connection = connection

    def create(self, title: str, equipment_id: int | None = None):
        sql = "INSERT INTO items (title, equipment_id) VALUES (?, ?)"
        cursor = self.connection.cursor()
        cursor.execute(sql, (title, equipment_id,))
        self.connection.commit()
        
    def get_by_id(self, item_id: int):
        sql = "SELECT * FROM items WHERE id = ?"
        cursor = self.connection.cursor()
        cursor.execute(sql, (item_id,))
        item = cursor.fetchone()
        return Item(**{key : item[i] for i, key in enumerate(Item.model_fields.keys())})
