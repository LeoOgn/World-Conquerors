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

class EquipmentRepository:
    def __init__(self, connection: Connection):
        self.connection = connection

    