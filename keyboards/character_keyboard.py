from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from aiogram import types


class CharacterCallback(CallbackData, prefix="character"):
    action: str
    


def character_keyboard(available_scores: int) -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    if available_scores > 0:
        builder.button(text=f"Повысить характеристики ({available_scores})", callback_data=CharacterCallback(action="score_up"))
    builder.button(text="Инвентарь", callback_data=CharacterCallback(action="inventory"))
    builder.button(text="Экипировка", callback_data=CharacterCallback(action="equipment"))
    builder.adjust(3 if available_scores > 0 else 2)
    return builder.as_markup()