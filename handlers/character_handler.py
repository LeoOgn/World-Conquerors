from services import CharacterService
from aiogram import types
from aiogram.fsm.context import FSMContext
from keyboards import character_keyboard


class CharacterHandler:
    def __init__(self, character_service: CharacterService):
        self.character_service = character_service
    async def character_handler(self, msg: types.Message):
        character = self.character_service.get_by_user_id(msg.from_user.id)
        await msg.answer(f"Данные о герое:\nУровень: {character.level}\nОпыт до следующего уровня: {character.experience}\nБаланс: {character.balance}\nСила: {character.streight}\nТелосложение: {character.phisyque}\nЛовкость: {character.agility}", reply_markup=character_keyboard(0))