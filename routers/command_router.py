from handlers import StartHandler, CreateCharacterState
from aiogram import Dispatcher
from aiogram.filters.command import Command

from keyboards.inline_main_menu_keyboard import MainMenuCallback


class CommandRouter:
    def __init__(self, dp: Dispatcher, start_handler: StartHandler):
        self.start_handler = start_handler
        self.dp = dp
        self._setup_routes()

    def _setup_routes(self):
        self.dp.message.register(self.start_handler.start_command, Command("start"))
        self.dp.callback_query.register(self.start_handler.handle, MainMenuCallback.filter())
        self.dp.message.register(self.start_handler.get_character_name, CreateCharacterState.name)