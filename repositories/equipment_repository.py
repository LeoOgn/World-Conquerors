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


class EquipmentRepository:
    def __init__(self, connection: Connection):
        self.connection = connection

    def create(self, title: str, bonus_streight: int, bonus_agility: int, bonus_phisyque: int, must_level: int, must_agility: int, must_phisyque: int, attack: int, defend: int, price: int, rare: str):
        sql = "INSERT INTO equipments (title, bonus_streight, bonus_agility, bonus_phisyque, must_level, must_agility, must_phisyque, attack, defend, price, rare) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cursor = self.connection.cursor()
        cursor.execute(sql, (title, bonus_streight, bonus_agility, bonus_phisyque, must_level, must_agility, must_phisyque, attack, defend, price, rare))
        self.connection.commit()
    