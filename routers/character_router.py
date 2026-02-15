from handlers import CharacterHandler
from aiogram import Dispatcher, F
from keyboards import CharacterCallback, AddScoresCallback, MainMenuCallback



class CharacterRouter:
    def __init__(self, dp: Dispatcher, character_handler: CharacterHandler):
        self.character_handler = character_handler
        self.dp = dp
        self._setup_routes()

    def _setup_routes(self):
        self.dp.message.register(self.character_handler.character_handler, F.text == "Персонаж 🧔🏻‍♀️")
        # self.dp.callback_query.register(self.character_handler.inline_character_handler, MainMenuCallback.filter())
        self.dp.callback_query.register(self.character_handler.character_menu_handler, CharacterCallback.filter())
        self.dp.callback_query.register(self.character_handler.score_up_handler, AddScoresCallback.filter())
