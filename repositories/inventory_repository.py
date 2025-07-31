from sqlite3 import Connection, connect
from typing import List
from pydantic import BaseModel

class Inventory(BaseModel):
    character_id: int
    item_id: int
    count: int
    is_equiped: bool



class InventoryRepository:
    def __init__(self, connection: Connection):
        self.connection = connection

    def add_item(self, character_id: int, item_id: int):
        sql = "INSERT INTO inventory (character_id, item_id) VALUES (?, ?)"
        cursor = self.connection.cursor()
        cursor.execute(sql, (character_id, item_id,))
        self.connection.commit()

    def get_items_by_character_id(self, character_id: int) -> List[Inventory]:
        sql = """
            SELECT items.title, inventory.count FROM inventory 
            LEFT JOIN items ON inventory.item_id = items.id
            LEFT JOIN equipment ON items.equipment_id = equipment.id
            WHERE inventory.character_id = ?
        """

        cursor = self.connection.cursor()
        cursor.execute(sql, (character_id,))
        inventory = cursor.fetchall()
        print(inventory)
        # return [
        #     Inventory(**{key : inv[i] for i, key in enumerate(Inventory.model_fields.keys())})
        #     for inv in inventory
        # ]
    
    def update_item_count(self, character_id: int, item_id: int, count: int):
        sql = "UPDATE inventory SET count = ? WHERE character_id = ? AND item_id = ?"
        cursor = self.connection.cursor()
        cursor.execute(sql, (count, character_id, item_id,))
        self.connection.commit()

    def get_inventory_by_item_id(self, character_id: int, item_id: int) -> Inventory | None:
        sql = "SELECT * FROM inventory WHERE character_id = ? AND item_id = ?"
        cursor = self.connection.cursor()
        cursor.execute(sql, (character_id, item_id,))
        inventory = cursor.fetchone()
        if not inventory: return None
        return Inventory(**{key : inventory[i] for i, key in enumerate(Inventory.model_fields.keys())})
