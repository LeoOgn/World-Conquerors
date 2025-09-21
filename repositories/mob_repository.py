# from sqlite3 import Connection, connect
from typing import List
from pymysql import Connection
from pymysql.cursors import DictCursor
from pydantic import BaseModel


class Mob(BaseModel):
    id: int
    name: str
    streight: int
    agility: int
    physique: int
    level: int
    location_id: int
    exp: int


class MobRepository:
    def __init__(self, connection: Connection):
        self.connection = connection

    def create(self, name: str, streight: int, agility: int, physique: int, level: int, location_id: int, exp: int):
        sql = "INSERT INTO mobs (name, streight, agility, physique, level, location_id, exp) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor = self.connection.cursor()
        cursor.execute(sql, (name, streight, agility, physique, level, location_id, exp))
        self.connection.commit()

    def get_all(self) -> List[tuple]:
        sql = "SELECT * FROM mobs"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
    
    def get_by_location_id(self, location_id: int):
        sql = "SELECT * FROM mobs WHERE location_id = %s"
        cursor = self.connection.cursor()
        cursor.execute(sql, (location_id,))
    
        mobs = cursor.fetchall()
        return [
            Mob(**mob)
            for mob in mobs
        ]
    
    def get_by_id(self, mob_id: int) -> Mob:
        sql = "SELECT * FROM mobs WHERE id = %s"
        cursor = self.connection.cursor()
        cursor.execute(sql, (mob_id,))
        mob = cursor.fetchone()
        return Mob(**mob)
    