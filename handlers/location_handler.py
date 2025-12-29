from services import LocationService, FightService
from aiogram import types
from aiogram.fsm.context import FSMContext
from keyboards import locations_keyboard, LocationCallback, prefight_keyboard, PrefightCallback, fight_keyboard, MainMenuCallback


class LocationHandler:
    def __init__(self, location_service: LocationService, fight_service: FightService):
        self.location_service = location_service
        self.fight_service = fight_service


    async def location_menu(self, msg: types.Message, state: FSMContext):
        locations = self.location_service.get_all()
        await msg.answer(
            "Выбери, путник, в какой локации будет твой путь.",
            reply_markup=locations_keyboard(locations)
        )

    async def inline_location_menu(self, callback: types.CallbackQuery):
        locations = self.location_service.get_all()

        await callback.message.edit_media(
            media=types.InputMediaPhoto(
            media=types.FSInputFile("images/Распутье.jpg"), caption=f"Выбери, путник, в какой локации будет пролегать твой путь."),
            reply_markup=locations_keyboard(locations)
        )
    
    async def choose_location(self, callback: types.CallbackQuery, callback_data: LocationCallback, state: FSMContext):
        location_id = callback_data.id
        location_title = callback_data.title
        await state.update_data(location_id=location_id)
        mob = self.location_service.get_random_mob(location_id)
        await callback.message.edit_text(
            f"Вы вошли в локацию {location_title}\nВы встретили {mob.name} ({mob.level} уровень)",
            reply_markup=prefight_keyboard(mob)
        )

    async def prefight_handler(self, callback: types.CallbackQuery, callback_data: PrefightCallback, state: FSMContext):
        if callback_data.action == "fight":
            self.fight_service.add_fight(callback.from_user.id, callback_data.mob_id)
            fight_info = self.fight_service.get_fight(callback.from_user.id)
            await callback.message.edit_text(
                f"Вы приняли бой с {fight_info.mob.name}\nТекущее здоровье противника: {fight_info.mob_health}\nВаше текущие здоровье: {fight_info.character.current_health}\nДа начнется бой!", 
                reply_markup=fight_keyboard()
            )
        elif callback_data.action == "search":
            data = await state.get_data()
            location_id = data.get("location_id")
            mob = self.location_service.get_random_mob(location_id)
            await callback.message.edit_text(
                f"Вы проигнорировали прошлого монстра и продолжили свой путь, путешествуя дальше, вы наткнулись на {mob.name} ({mob.level} уровень)",
                reply_markup=prefight_keyboard(mob)
            )