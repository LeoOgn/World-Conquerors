from handlers import CharacterHandler
from aiogram import Dispatcher, F



class CharacterRouter:
    def __init__(self, dp: Dispatcher, character_handler: CharacterHandler):
        self.character_handler = character_handler
        self.dp = dp
        self._setup_routes()

    def _setup_routes(self):
        self.dp.message.register(self.character_handler.character_handler, F.text == "Персонаж 🧔🏻‍♀️")