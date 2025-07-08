from sqlite3 import Connection, connect
from typing import List


class MobRepository:
    def __init__(self, connection: Connection):
        self.connection = connection

    def create(self, name: str, streight: int, agility: int, physique: int, level: int, location_id: int):
        sql = "INSERT INTO mobs (name, streight, agility, physique, level, location_id) VALUES (?, ?, ?, ?, ?, ?)"
        cursor = self.connection.cursor()
        cursor.execute(sql, (name, streight, agility, physique, level, location_id))
        self.connection.commit()

    def get_all(self) -> List[tuple]:
        sql = "SELECT * FROM mobs"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        return cursor.fetchall()