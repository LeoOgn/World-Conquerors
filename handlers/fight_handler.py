from services import FightService
from aiogram import types
from keyboards import FightCallback


class FightHandler:
    def __init__(self, fight_service: FightService):
        self.fight_service = fight_service

    def fight_handler(self, callback: types.CallbackQuery, callback_data: FightCallback):
        if callback_data.action == "hit":
            ...