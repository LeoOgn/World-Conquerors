# from sqlite3 import Connection, connect
from typing import List
from pymysql import Connection
from pymysql.cursors import DictCursor
from pydantic import BaseModel
from datetime import datetime


class Location(BaseModel):
    id: int
    title: str
    level_from: int
    level_to: int
    created: datetime


class LocationRepository:
    def __init__(self, connection: Connection):
        self.connection = connection

    def clear(self):
        sql = "DELETE FROM locations"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        self.connection.commit()

    def create(self, title: str, level_from: str, level_to: int):
        sql = "INSERT INTO locations (title, level_from, level_to) VALUES (%s, %s, %s)"
        cursor = self.connection.cursor()
        cursor.execute(sql, (title, level_from, level_to))
        self.connection.commit()

    def get_all(self) -> List[Location]:
        sql = "SELECT * FROM locations"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        locations = cursor.fetchall()
        return [
            Location(**location)
            for location in locations
        ]
    
    def get_by_id(self, location_id: int) -> Location:
        sql = "SELECT * FROM locations WHERE id = %s"
        cursor = self.connection.cursor()
        cursor.execute(sql, (location_id,))
        location = cursor.fetchone()
        return Location(**location)