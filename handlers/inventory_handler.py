from aiogram import types
from services import InventoryService, CharacterService
from keyboards import InventoryCallback, character_keyboard, item_keyboard, ItemCallback, inventory_keyboard


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
            await callback.message.edit_media(
                media=types.InputMediaPhoto(
                    media=types.FSInputFile("images/Персонаж.png"), caption=f"Данные о герое:\nУровень: {character.level}\nОпыт до следующего уровня: {character.experience}\nБаланс: {character.balance}\nСила: {character.streight}\nТелосложение: {character.physique}\nЛовкость: {character.agility}"),
                    reply_markup=character_keyboard(character.available_scores)
            )
        elif callback_data.action == "show":
            item_info = self.inventory_service.get_item(callback_data.item_id)
            print(item_info)
            photo=item_info.image if item_info.image is not None else "images/Пусто.png"
            if item_info.equipment:
                await callback.message.edit_media(
                    media=types.InputMediaPhoto(
                        media=types.FSInputFile(photo), caption=f"{item_info.title}\nЦена: {item_info.price}\nБонус ловкости: {item_info.equipment.bonus_agility}\nБонус силы: {item_info.equipment.bonus_streight}\nБонус телосложения: {item_info.equipment.bonus_physique}\nАтака: {item_info.equipment.attack}\nБроня: {item_info.equipment.defend}\n{item_info.description}",
                    ),
                    reply_markup=item_keyboard()
                )
            else:
                await callback.message.edit_media(
                    media=types.InputMediaPhoto(
                        media=types.FSInputFile(photo), caption=f"{item_info.title}\nЦена: {item_info.price}\n{item_info.description}",
                    ),
                    reply_markup=item_keyboard()
                )
    
    async def item_handler(self, callback: types.CallbackQuery, callback_data: ItemCallback):
        if callback_data.action == "back":
            character = self.character_service.get_by_user_id(callback.from_user.id)
            inventory = self.inventory_service.get_inventory(character.id)
            await callback.message.edit_media(
                media=types.InputMediaPhoto(
                    media=types.FSInputFile("images/Инвентарь.png"), caption="Инвентарь",
                ),
                reply_markup=inventory_keyboard(inventory)
            )