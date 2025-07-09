from services import LocationService
from aiogram import types
from aiogram.fsm.context import FSMContext
from keyboards import locations_keyboard, LocationCallback


class LocationHandler:
    def __init__(self, location_service: LocationService):
        self.location_service = location_service

    async def location_menu(self, msg: types.Message, state: FSMContext):
        locations = self.location_service.get_all()
        await msg.answer(
            "Выбери, путник, в какой локации будет твой путь.",
            reply_markup=locations_keyboard(locations)
        )
    
    async def choose_location(self, callback: types.CallbackQuery, callback_data: LocationCallback):
        location_id = callback_data.id
        location_title = callback_data.title
        await callback.message.edit_text(
            f"Вы вошли в локацию {location_title}",
            reply_markup=None
        )
