from services import LocationService
from aiogram import types
from aiogram.fsm.context import FSMContext


class LocationHandler:
    def __init__(self, location_service: LocationService):
        self.location_service = location_service

    async def location_menu(self, msg: types.Message, state: FSMContext):
        locations = self.location_service.get_all()
        print("locations", locations)
        await msg.answer("Выбери, путник, в какой локации будет твой путь.")