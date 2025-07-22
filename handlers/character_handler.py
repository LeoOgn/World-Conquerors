from services import CharacterService
from aiogram import types
from aiogram.fsm.context import FSMContext
from keyboards import character_keyboard, add_scores_keyboard, NewScores, CharacterCallback


class CharacterHandler:
    def __init__(self, character_service: CharacterService):
        self.character_service = character_service

    async def character_handler(self, msg: types.Message):
        character = self.character_service.get_by_user_id(msg.from_user.id)
        await msg.answer(f"Данные о герое:\nУровень: {character.level}\nОпыт до следующего уровня: {character.experience}\nБаланс: {character.balance}\nСила: {character.streight}\nТелосложение: {character.phisyque}\nЛовкость: {character.agility}", reply_markup=character_keyboard(character.available_scores))

    async def character_menu_handler(self, callback: types.CallbackQuery, callback_data: CharacterCallback):
        if callback_data.action == "score_up":
            character = self.character_service.get_by_user_id(callback.from_user.id)
            await callback.message.edit_text(
                text="Распределите характеристики", 
                reply_markup=add_scores_keyboard(character, NewScores())
            )