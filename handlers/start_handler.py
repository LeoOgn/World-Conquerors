from services import UserService
from keyboards import main_menu_keyboard
from aiogram import types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


class CreateCharacterState(StatesGroup):
    name = State()


class StartHandler:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    async def start_command(self, msg: types.Message, state: FSMContext):
        # self.user_service.signup(msg.from_user.id, msg.from_user.username)
        await msg.answer("Здравствуй путник! Как зовут тебя?")
        await state.set_state(CreateCharacterState.name)