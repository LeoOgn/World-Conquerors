from repositories import MobRepository, Mob, CharacterRepository, Character
from pydantic import BaseModel

class FightInfo(BaseModel):
    mob: Mob
    character: Character
    mob_health: int


class FightService:
    def __init__(self, mob_repository: MobRepository, character_repository: CharacterRepository):
        self.fights = {}
        self.mob_repository = mob_repository
        self.character_repository = character_repository

    def add_fight(self, player_id: int, mob_id: int):
        mob = self.mob_repository.get_by_id(mob_id)
        character = self.character_repository.get_by_user_id(player_id)
        self.fights[player_id] = FightInfo(
            mob = mob,
            character=character,
            mob_health=mob.phisyque*5
        )

    def get_fight(self, player_id: int) -> FightInfo:
        return self.fights.get(player_id)

    def on_hit(self, player_id: int) -> FightInfo:
        fight = self.get_fight(player_id)
        mob_dmg = fight.character.streight*5 - fight.mob.phisyque
        fight.mob_health -= mob_dmg

        character_dmg = fight.mob.streight*5 - fight.character.phisyque
        fight.character.current_health -= character_dmg

        self.character_repository.update_character_health(fight.character.current_health, fight.character.current_health)
        