from aiogram import types
from services import InventoryService
from keyboards import InventoryCallback, character_keyboard


class InventoryHandler:
    def __init__(self, inventory_service: InventoryService):
        self.inventory_service = inventory_service
        
    async def inventory_handler(self, callback: types.CallbackQuery, callback_data: InventoryCallback):
        if callback_data.action == "back":
            character = self.character_service.get_by_user_id(callback.from_user.id)
            await callback.message.edit_text(
                text=f"Данные о герое:\nУровень: {character.level}\nОпыт до следующего уровня: {character.experience}\nБаланс: {character.balance}\nСила: {character.streight}\nТелосложение: {character.physique}\nЛовкость: {character.agility}", reply_markup=character_keyboard(character.available_scores)
            )
        elif callback_data.action == "show":
            ...