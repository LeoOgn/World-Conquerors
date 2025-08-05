from repositories import MobRepository, Mob, CharacterRepository, Character
from pydantic import BaseModel
from random import randint

class FightInfo(BaseModel):
    status: str = "in_process"
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
            mob_health=mob.physique*3
        )

    def get_fight(self, player_id: int) -> FightInfo:
        return self.fights.get(player_id)

    def _can_level_up(self, character: Character) -> bool:
        must_exp = 2 ** character.level
        return character.experience >= must_exp
    def on_hit(self, player_id: int) -> FightInfo:
        fight = self.get_fight(player_id)
        mob_dmg = fight.character.streight
        if mob_dmg < 0: mob_dmg = 0
        print("mob_dmg", mob_dmg)
        mob_evasion = fight.mob.agility - fight.character.agility
        if mob_evasion < 0: mob_evasion = 0
        chance = randint(1, 100)
        if chance > mob_evasion:
            fight.mob_health -= mob_dmg

        character_dmg = fight.mob.streight
        if character_dmg < 0: character_dmg = 0
        print("character_dmg", character_dmg)

        character_evasion = fight.character.agility - fight.mob.agility
        if character_evasion < 0: character_evasion = 0
        chance = randint(1, 100)
        if chance > character_evasion:
            fight.character.current_health -= character_dmg

        self.character_repository.update_character_health(fight.character.current_health, fight.character.current_health)

        if fight.mob_health <= 0 and fight.character.current_health <= 0:
            gain_exp = fight.mob.exp
            fight.character.experience += gain_exp
            self.character_repository.update_character_experience(fight.character.experience, fight.character.id)
            if self._can_level_up(fight.character):
                self.character_repository.level_up(player_id)
            fight.status = "draw"
            fight.character = self.character_repository.get_by_user_id(player_id)
            return fight
        
        if fight.mob_health <= 0 and fight.character.current_health > 0:
            gain_exp = fight.mob.exp
            fight.character.experience += gain_exp
            self.character_repository.update_character_experience(fight.character.experience, fight.character.id)
            if self._can_level_up(fight.character):
                self.character_repository.level_up(player_id)
            fight.status = "win"
            fight.character = self.character_repository.get_by_user_id(player_id)
            return fight
        
        if fight.mob_health > 0 and fight.character.current_health <= 0:
            fight.character.experience = 0
            fight.status = "loose"
            return fight

        return fight