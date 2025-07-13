from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from aiogram import types
from repositories import Mob


class PrefightCallback(CallbackData, prefix="prefight"):
    action: str
    mob_id: int | None = None
    


def prefight_keyboard(mob: Mob) -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="Принять бой 🥊", callback_data=PrefightCallback(action="fight", mob_id=mob.id))
    builder.button(text="Найти другого соперника ➡️", callback_data=PrefightCallback(action="search"))
    builder.button(text="Отправиться в город 🏙️", callback_data=PrefightCallback(action="return"))
    builder.adjust(3)
    return builder.as_markup()