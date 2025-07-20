from sqlite3 import Connection, connect
from pydantic import BaseModel

class Character(BaseModel):
    id: int
    name: str
    streight: int
    agility: int
    phisyque: int
    level: int
    balance: int
    experience: int
    current_health: int

class CharacterRepository:
    def __init__(self, connection: Connection):
        self.connection = connection

    def create(self, name: str, user_id: int):
        sql = "INSERT INTO characters (name, user_id) VALUES (?, ?)"
        cursor = self.connection.cursor()
        cursor.execute(sql, (name, user_id))
        self.connection.commit()

    def get_by_user_id(self, user_id: int) -> Character:
        sql = "SELECT * FROM characters WHERE user_id = ?"
        cursor = self.connection.cursor()
        cursor.execute(sql, (user_id,))
        character = cursor.fetchone()
        return Character(**{key : character[i] for i, key in enumerate(Character.model_fields.keys())})

    def update_character_health(self, new_value: int, character_id: int):
        sql = "UPDATE characters SET current_health = ? WHERE id = ?"
        if new_value < 0:
            new_value = 0
        cursor = self.connection.cursor()
        cursor.execute(sql, (new_value, character_id))
        self.connection.commit()
    