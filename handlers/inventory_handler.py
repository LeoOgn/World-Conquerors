from aiogram import types
from services import InventoryService, CharacterService
from keyboards import InventoryCallback, character_keyboard


class InventoryHandler:
    def __init__(
        self, 
        inventory_service: InventoryService,
        character_service: CharacterService
    ):
        self.inventory_service = inventory_service
        self.character_service = character_service
        
    async def inventory_handler(self, callback: types.CallbackQuery, callback_data: InventoryCallback):
        if callback_data.action == "back":
            character = self.character_service.get_by_user_id(callback.from_user.id)
            await callback.message.edit_text(
                text=f"Данные о герое:\nУровень: {character.level}\nОпыт до следующего уровня: {character.experience}\nБаланс: {character.balance}\nСила: {character.streight}\nТелосложение: {character.physique}\nЛовкость: {character.agility}", reply_markup=character_keyboard(character.available_scores)
            )
        elif callback_data.action == "show":
            item_info = self.inventory_service.get_item(callback_data.item_id)
            print(item_info)
            await callback.message.edit_text(
                text=f"{item_info.title}\nЦена: {item_info.price}"
            )