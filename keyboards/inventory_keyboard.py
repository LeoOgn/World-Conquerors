from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from repositories import UserInventory
from typing import List
from aiogram import types


class InventoryCallback(CallbackData, prefix="inventory"):
    action: str
    item_id: int | None = None

def inventory_keyboard(inventory: List[UserInventory]) -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for item in inventory:
        builder.button(text=f"{item.item_title} ({item.count})", callback_data=InventoryCallback(action="show", item_id=item.item_id))
    builder.button(text="Назад", callback_data=InventoryCallback(action="back"))
    builder.adjust(1)
    return builder.as_markup()

