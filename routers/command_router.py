from handlers import StartHandler
from aiogram import Dispatcher
from aiogram.filters.command import Command


class CommandRouter:
    def __init__(self, dp: Dispatcher, start_handler: StartHandler):
        self.start_handler = start_handler
        self.dp = dp
        self._setup_routes()

    def _setup_routes(self):
        self.dp.message.register(self.start_handler.start_command, Command("start"))