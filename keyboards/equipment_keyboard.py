from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from aiogram import types


class EquipmentCallback(CallbackData, prefix="equipment"):
    action: str
    type_id: int | None = None
    


def equipment_keyboard() -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="Головной убор", callback_data=EquipmentCallback(action="show", type_id=1))
    builder.button(text="Тело", callback_data=EquipmentCallback(action="show", type_id=2))
    builder.button(text="Ноги", callback_data=EquipmentCallback(action="show", type_id=3))
    builder.button(text="Обувь", callback_data=EquipmentCallback(action="show", type_id=4))
    builder.button(text="Аксессуар", callback_data=EquipmentCallback(action="show", type_id=5))
    builder.button(text="Аксессуар", callback_data=EquipmentCallback(action="show", type_id=5))
    builder.button(text="Оружие", callback_data=EquipmentCallback(action="show", type_id=6))
    builder.button(text="Назад", callback_data=EquipmentCallback(action="back"))
    builder.adjust(1)
    return builder.as_markup()