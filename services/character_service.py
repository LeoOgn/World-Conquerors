from repositories import CharacterRepository


class CharacterService:
    def __init__(self, character_repo: CharacterRepository):
        self.character_repo = character_repo
    
    def create_character(self, name: str, user_id: int):
        self.character_repo.create(name, user_id)
        print(f"{user_id} creates {name}")