from services import UserService
from aiogram import types


class StartHandler:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    async def start_command(self, msg: types.Message):
        print(msg.from_user.username, msg.from_user.full_name, msg.from_user.id)
        self.user_service.signup(msg.from_user.id, msg.from_user.username)
        await msg.answer("Здравствуй путник! Как зовут тебя?!")