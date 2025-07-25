from sqlite3 import Connection, connect
from pydantic import BaseModel

class Equipment(BaseModel):
    id: int
    title: str
    bonus_streight: int
    bonus_agility: int
    bonus_phisyque: int
    must_level: int
    must_streight: int
    must_agility: int
    must_phisyque: int
    attack: int
    defend: int
    price: int
    rare: str
    equipment_type_id: int
    equipment_set_id: int | None = None


class EquipmentRepository:
    def __init__(self, connection: Connection):
        self.connection = connection

    def create(self, title: str, bonus_streight: int, bonus_agility: int, bonus_phisyque: int, must_level: int, must_agility: int, must_phisyque: int, attack: int, defend: int, price: int, rare: str, type_id: int, set_id: int = None):
        sql = "INSERT INTO equipments (title, bonus_streight, bonus_agility, bonus_phisyque, must_level, must_agility, must_phisyque, attack, defend, price, rare, equipment_type_id, equipment_set_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cursor = self.connection.cursor()
        cursor.execute(sql, (title, bonus_streight, bonus_agility, bonus_phisyque, must_level, must_agility, must_phisyque, attack, defend, price, rare, type_id, set_id))
        self.connection.commit()

    def create_set(self, title: str, bonus_streight: int, bonus_agility: int, bonus_phisyque: int):
        sql = "INSERT INTO equipment_sets (title, bonus_streight, bonus_agility, bonus_phisyque) VALUES (?, ?, ?, ?)"
        cursor = self.connection.cursor()
        cursor.execute(sql, (title, bonus_streight, bonus_agility, bonus_phisyque))
        self.connection.commit()

    def create_type(self, title: str):
        sql = "INSERT INTO equipment_sets (title) VALUES (?)"
        cursor = self.connection.cursor()
        cursor.execute(sql, (title))
        self.connection.commit()