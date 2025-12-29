from handlers.character_handler import CharacterHandler
from handlers.location_handler import LocationHandler
from services import CharacterService, InventoryService
from aiogram import types
from aiogram.fsm.context import FSMContext
from keyboards import (character_keyboard, add_scores_keyboard, NewScores, CharacterCallback, AddScoresCallback, MainMenuCallback)
from repositories import Character
from keyboards import inventory_keyboard, equipment_keyboard


class MainMenuHandler:
    def __init__(
        self, 
        character_handler: CharacterHandler,
        location_handler: LocationHandler
    ):
        self.character_handler = character_handler
        self.location_handler = location_handler

    async def handle(self, callback: types.CallbackQuery, callback_data: MainMenuCallback):
        match callback_data.action:
            case "character":
                await self.character_handler.inline_character_handler(callback)
            case "wasteland":
                await self.location_handler.inline_location_menu(callback)