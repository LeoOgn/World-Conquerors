from services import CharacterService, InventoryService
from aiogram import types
from aiogram.fsm.context import FSMContext
from keyboards import (character_keyboard, EquipmentCallback)
from repositories import Character
from keyboards import inventory_keyboard, equipment_keyboard


class EquipmentHandler:
    def __init__(
        self, 
        character_service: CharacterService,
        inventory_service: InventoryService
    ):
        self.character_service = character_service
        self.inventory_service = inventory_service

    async def equipment_handler_menu(self, callback: types.CallbackQuery, callback_data: EquipmentCallback, state: FSMContext):
        character = self.character_service.get_by_user_id(callback.from_user.id)
        if callback_data.action == 'back':
            await callback.message.edit_media(
                media=types.InputMediaPhoto(
                    media=types.FSInputFile("images/Персонаж.png"), caption=f"Данные о герое:\nУровень: {character.level}\nОпыт до следующего уровня: {character.experience}\nБаланс: {character.balance}\nСила: {character.streight}\nТелосложение: {character.physique}\nЛовкость: {character.agility}",
                ), 
                reply_markup=character_keyboard(character.available_scores)
            )