from sqlite3 import Connection
from pydantic import BaseModel


class Loot(BaseModel):
    mob_id: int
    item_id: int
    chance: float


class LootRepository:
    def __init__(self, connection: Connection):
        self.connection = connection
        
    def create(self, loot: Loot):
        sql = "INSERT INTO loot (mob_id, item_id, chance) VALUES (?, ?, ?)"
        cursor = self.connection.cursor()
        cursor.execute(sql, (loot.mob_id, loot.item_id, loot.chance))
        self.connection.commit()