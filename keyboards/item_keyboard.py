from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from aiogram import types
from typing import List

class ItemCallback(CallbackData, prefix="item"):
    action: str

def item_keyboard() -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="Назад", callback_data=ItemCallback(action="back"))
    builder.adjust(1)
    return builder.as_markup()