from handlers import FightHandler
from aiogram import Dispatcher, F
from keyboards import FightCallback



class FightsRouter:
    def __init__(self, dp: Dispatcher, fight_handler: FightHandler):
        self.fight_handler = fight_handler
        self.dp = dp
        self._setup_routes()

    def _setup_routes(self):
        self.dp.callback_query.register(self.fight_handler.fight_handler, FightCallback.filter())