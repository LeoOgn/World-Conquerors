# from sqlite3 import Connection, connect
from pymysql import Connection
from pymysql.cursors import DictCursor
from pydantic import BaseModel

class Character(BaseModel):
    id: int
    name: str
    streight: int
    agility: int
    physique: int
    level: int
    balance: int
    experience: int
    current_health: int
    available_scores: int

class CharacterRepository:
    def __init__(self, connection: Connection):
        self.connection = connection

    def create(self, name: str, user_id: int):
        sql = "INSERT INTO characters (name, user_id) VALUES (%s, %s)"
        cursor: DictCursor = self.connection.cursor()
        cursor.execute(sql, (name, user_id))
        self.connection.commit()

    def get_by_user_id(self, user_id: int) -> Character:
        sql = "SELECT * FROM characters WHERE user_id = %s"
        cursor = self.connection.cursor()
        cursor.execute(sql, (user_id,))
        character = cursor.fetchone()
        return Character(**character)

    def update_character_health(self, new_value: int, character_id: int):
        sql = "UPDATE characters SET current_health = %s WHERE id = %s"
        if new_value < 0:
            new_value = 0
        cursor = self.connection.cursor()
        cursor.execute(sql, (new_value, character_id))
        self.connection.commit()

    def level_up(self, user_id: int):
        sql = "UPDATE characters SET level = %s, experience = %s, available_scores = %s WHERE id = %s"
        character = self.get_by_user_id(user_id)
        experience = character.experience - 2 ** character.level
        level = character.level + 1
        scores = character.available_scores + 5
        cursor = self.connection.cursor()
        cursor.execute(sql, (level, experience, scores, character.id,))
        self.connection.commit()

    def update_character_experience(self, new_value: int, character_id: int):
        sql = "UPDATE characters SET experience = %s WHERE id = %s"
        cursor = self.connection.cursor()
        cursor.execute(sql, (new_value, character_id))
        self.connection.commit()

    def update_character_scores(self, character: Character):
        sql = "UPDATE characters SET streight = %s, agility = %s, physique = %s, available_scores = %s WHERE id = %s"
        cursor = self.connection.cursor()
        cursor.execute(sql, (
            character.streight, 
            character.agility, 
            character.physique, 
            character.available_scores,
            character.id
        ))
        self.connection.commit()
    
