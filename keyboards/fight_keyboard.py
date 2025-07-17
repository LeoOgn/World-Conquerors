from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from aiogram import types
from repositories import Mob


class FightCallback(CallbackData, prefix="fight"):
    action: str
    


def fight_keyboard() -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="Нанести удар", callback_data=FightCallback(action="hit"))
    builder.button(text="Использовать дополнительные предметы", callback_data=FightCallback(action="use_item"))
    builder.adjust(2)
    return builder.as_markup()