from repositories import CharacterRepository, Character
from keyboards import NewScores


class CharacterService:
    def __init__(self, character_repo: CharacterRepository):
        self.character_repo = character_repo
    
    def create_character(self, name: str, user_id: int):
        self.character_repo.create(name, user_id)
        print(f"{user_id} creates {name}")

    def get_by_user_id(self, user_id:int):
        return self.character_repo.get_by_user_id(user_id)
    
    def update_scores(self, character: Character, scores: NewScores):
        character.streight += scores.streight
        character.agility += scores.agility
        character.physique += scores.physique
        character.current_health = character.physique * 3

        self.character_repo.update_character_scores(character)
        self.character_repo.update_character_health(character.current_health, character.id)