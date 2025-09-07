# from sqlite3 import Connection, connect
from pydantic import BaseModel
from pymysql import Connection
from pymysql.cursors import DictCursor


class Item(BaseModel):
    id: int
    title: str
    rare: str
    description: str
    price: int
    equipment_id: int | None = None
    image: str | None = None
    
class ItemRepository:
    def __init__(self, connection: Connection):
        self.connection = connection

    def create(self, 
               title: str, rare: str, description: str, 
               price: int, equipment_id: int | None = None, image: str | None = None
            ):
        sql = "INSERT INTO items (title, rare, description, price, equipment_id, image) VALUES (?, ?, ?, ?, ?, ?)"
        cursor = self.connection.cursor()
        cursor.execute(sql, (title, rare, description, price, equipment_id, image))
        self.connection.commit()
        
    def get_by_id(self, item_id: int):
        sql = "SELECT * FROM items WHERE id = ?"
        cursor = self.connection.cursor()
        cursor.execute(sql, (item_id,))
        item = cursor.fetchone()
        return Item(**item.items())
