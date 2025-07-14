from repositories import MobRepository, Mob, CharacterRepository, Character
from pydantic import BaseModel

class FightInfo(BaseModel):
    mob: Mob


class FightService:
    def __init__(self, mob_repository: MobRepository, character_repository: CharacterRepository):
        self.fights = {}
        self.mob_repository = mob_repository
        self.character_repository = character_repository

    def add_fight(self, player_id: int, mob_id: int):
        mob = self.mob_repository.get_by_id(mob_id)
        character = self.character_repository.get_by_user_id(player_id)