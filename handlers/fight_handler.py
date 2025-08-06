from services import FightService, LocationService, InventoryService
from aiogram import types
from aiogram.fsm.context import FSMContext
from keyboards import FightCallback, fight_keyboard, prefight_keyboard


class FightHandler:
    def __init__(
            self, 
            fight_service: FightService,
            location_service: LocationService,
            inventory_service: InventoryService
        ):
        self.fight_service = fight_service
        self.location_service = location_service
        self.inventory_service = inventory_service

    async def fight_handler(self, callback: types.CallbackQuery, callback_data: FightCallback, state: FSMContext):
        if callback_data.action == "hit":
            fight_info = self.fight_service.on_hit(callback.from_user.id)
            if fight_info.status == "in_process":
                await callback.message.edit_text(f"Вы нанесли удар, у противника осталось  {fight_info.mob_health} здоровья\nВам нанесли удар, у вас осталоcь {fight_info.character.current_health} здоровья", reply_markup=fight_keyboard())
            elif fight_info.status == "draw":
                await callback.message.edit_text(f"Вы убили вашего противника, но, к сожалению, тоже погибли!", reply_markup=None)
            elif fight_info.status == "win":
                data = await state.get_data()
                location_id = data.get("location_id", 1)
                mob = self.location_service.get_random_mob(location_id)
                print("INFO::: loot:", fight_info.loot)
                if fight_info.loot is not None:
                    for loot_item in fight_info.loot:
                        self.inventory_service.add_item(fight_info.character.id, loot_item)
                await callback.message.edit_text(f"Поздравляем! Вы победили в битве! После сражения вы наткнулись на {mob.name}", reply_markup=prefight_keyboard(mob))
            elif fight_info.status == "loose":
                await callback.message.edit_text(f"К сожалению, вам не хватило сил победить потивника, вы погибли!", reply_markup=None)