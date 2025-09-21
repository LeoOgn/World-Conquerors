# from sqlite3 import Connection, connect
from pymysql import Connection
from pymysql.cursors import DictCursor
from pydantic import BaseModel

class Equipment(BaseModel):
    id: int
    title: str
    bonus_streight: int
    bonus_agility: int
    bonus_physique: int
    must_level: int
    must_streight: int
    must_agility: int
    must_physique: int
    attack: int
    defend: int
    equipment_type_id: int
    equipment_set_id: int | None = None


class EquipmentRepository:
    def __init__(self, connection: Connection):
        self.connection = connection

    def create(self, title: str, bonus_streight: int, bonus_agility: int, bonus_physique: int, must_level: int, must_streight: int, must_agility: int, must_physique: int, attack: int, defend: int, equipment_type_id: int, equipment_set_id: int = None):
        sql = "INSERT INTO equipment (title, bonus_streight, bonus_agility, bonus_physique, must_level, must_streight, must_agility, must_physique, attack, defend, equipment_type_id, equipment_set_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor = self.connection.cursor()
        cursor.execute(sql, (title, bonus_streight, bonus_agility, bonus_physique, must_level,must_streight, must_agility, must_physique, attack, defend, equipment_type_id, equipment_set_id))
        self.connection.commit()

    def create_set(self, title: str, bonus_streight: int, bonus_agility: int, bonus_physique: int):
        sql = "INSERT INTO equipment_sets (title, bonus_streight, bonus_agility, bonus_physique) VALUES (%s, %s, %s, %s)"
        cursor = self.connection.cursor()
        cursor.execute(sql, (title, bonus_streight, bonus_agility, bonus_physique))
        self.connection.commit()

    def create_type(self, title: str):
        sql = "INSERT INTO equipment_types (title) VALUES (%s)"
        cursor = self.connection.cursor()
        cursor.execute(sql, (title,))
        self.connection.commit()

    def get_by_id(self, id: int) -> Equipment:
        sql = "SELECT * FROM equipment WHERE id = %s"
        cursor = self.connection.cursor()
        cursor.execute(sql, (id,))
        equipment = cursor.fetchone()
        return Equipment(**equipment)