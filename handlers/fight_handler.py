from services import FightService
from aiogram import types
from keyboards import FightCallback, fight_keyboard


class FightHandler:
    def __init__(self, fight_service: FightService):
        self.fight_service = fight_service

    async def fight_handler(self, callback: types.CallbackQuery, callback_data: FightCallback):
        if callback_data.action == "hit":
            fight_info = self.fight_service.on_hit(callback.from_user.id)
            if fight_info.status == "in_process":
                await callback.message.edit_text(f"Вы нанесли удар, у противника осталось  {fight_info.mob_health} здоровья\nВам нанесли удар, у вас осталоcь {fight_info.character.current_health} здоровья", reply_markup=fight_keyboard())