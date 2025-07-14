from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from aiogram import types
from repositories import Mob


class FightCallback(CallbackData, prefix="fight"):
    action: str
    mob_id: int | None = None
    


def fight_keyboard(mob: Mob) -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="Нанести удар", callback_data=FightCallback(action="fight", mob_id=mob.id))
    builder.button(text="Использовать дополнительные предметы", callback_data=FightCallback(action="search"))
    builder.adjust(2)
    return builder.as_markup()