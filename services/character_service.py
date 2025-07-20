from repositories import CharacterRepository


class CharacterService:
    def __init__(self, character_repo: CharacterRepository):
        self.character_repo = character_repo
    
    def create_character(self, name: str, user_id: int):
        self.character_repo.create(name, user_id)
        print(f"{user_id} creates {name}")

    def get_by_user_id(self, user_id:int):
        return self.character_repo.get_by_user_id(user_id)