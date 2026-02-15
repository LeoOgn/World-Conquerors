from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from aiogram import types
from pydantic import BaseModel
from repositories import Character


class AddScoresCallback(CallbackData, prefix="add_scores"):
    action: str
    feature: str | None = None
    
class NewScores(BaseModel):
    streight: int = 0
    agility: int = 0
    physique: int = 0


def add_scores_keyboard(character: Character, new_scores: NewScores) -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    
    builder.button(text="-", callback_data=AddScoresCallback(action="dec", feature="streight"))
    builder.button(text=f"Сила {character.streight + new_scores.streight}", callback_data=AddScoresCallback(action="none"))
    builder.button(text="+", callback_data=AddScoresCallback(action="inc", feature="streight"))

    builder.button(text="-", callback_data=AddScoresCallback(action="dec", feature="agility"))
    builder.button(text=f"Ловкость {character.agility + new_scores.agility}", callback_data=AddScoresCallback(action="none"))
    builder.button(text="+", callback_data=AddScoresCallback(action="inc", feature="agility")) 

    builder.button(text="-", callback_data=AddScoresCallback(action="dec", feature="physique"))
    builder.button(text=f"Здоровье {character.physique + new_scores.physique}", callback_data=AddScoresCallback(action="none"))
    builder.button(text="+", callback_data=AddScoresCallback(action="inc", feature="physique"))

    builder.button(
        text=f"{character.available_scores} очков",
        callback_data=AddScoresCallback(action="none")
    )

    builder.button(
        text="Подтвердить",
        callback_data=AddScoresCallback(action="done")
    )

    builder.adjust(3, 3, 3, 1, 1)
    return builder.as_markup()