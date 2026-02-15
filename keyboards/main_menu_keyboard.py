from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import types


def main_menu_keyboard() -> types.ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(text="Рейтинг игроков 📊")
    builder.button(text="Магазин 🛍️")
    builder.button(text="Пустоши 🧛🏻")
    builder.button(text="Данжи 🛕")
    builder.button(text="Шахты ⛏️")
    builder.button(text="Арена ⚔️")
    builder.button(text="Персонаж 🧔🏻‍♀️")
    builder.adjust(3, 3, 1)
    return builder.as_markup(resize_keyboard=True)
