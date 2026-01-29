from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from aiogram import types
from repositories import Location
from typing import List


class LocationCallback(CallbackData, prefix="location"):
    id: int
    


def locations_keyboard(locations: List[Location]) -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for location in locations:
        builder.button(
            text=f"{location.title} ({location.level_from} - {location.level_to})", 
            callback_data=LocationCallback(id=location.id)
        )
    builder.adjust(1)
    return builder.as_markup()

        