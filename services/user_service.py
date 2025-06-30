from repositories import UserRepository


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo
    
    def signup(self, id: int, username: str):
        self.user_repo.create(id, username)
