from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from aiogram import types

class MainMenuCallback(CallbackData, prefix="main_menu"):
    action: str


def inline_main_menu_keyboard() -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="Рейтинг игроков 📊", callback_data=MainMenuCallback(action="raiting"))
    builder.button(text="Магазин 🛍️", callback_data=MainMenuCallback(action="shop"))
    builder.button(text="Пустоши 🧛🏻", callback_data=MainMenuCallback(action="wasteland"))
    builder.button(text="Данжи 🛕", callback_data=MainMenuCallback(action="danges"))
    builder.button(text="Шахты ⛏️", callback_data=MainMenuCallback(action="mines"))
    builder.button(text="Арена ⚔️", callback_data=MainMenuCallback(action="arena"))
    builder.button(text="Персонаж 🧔🏻‍♀️", callback_data=MainMenuCallback(action="character"))
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)
