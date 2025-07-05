from services import UserService, CharacterService
from keyboards import main_menu_keyboard
from aiogram import types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


class CreateCharacterState(StatesGroup):
    name = State()


class StartHandler:
    def __init__(
            self, 
            user_service: UserService,
            character_service: CharacterService
        ):
        self.user_service = user_service
        self.character_service = character_service

    async def start_command(self, msg: types.Message, state: FSMContext):
        if not self.user_service.check_auth(msg.from_user.id):
            self.user_service.signup(msg.from_user.id, msg.from_user.username)
            await msg.answer("Здравствуй путник! Как зовут тебя?")
            await state.set_state(CreateCharacterState.name)
        else:
            await msg.answer("Здравствуй, путник! Попытка повторной регистррации с твоей стороны возмутительна! Мы закроем на это глаза, продолжай охоту или добычу.", reply_markup=main_menu_keyboard())

    async def get_character_name(self, msg: types.Message, state: FSMContext):
        name = msg.text
        self.character_service.create_character(name, msg.from_user.id)
        await msg.answer("Поздравляем! Вы создали своего персонажа! Теперь только вам решать, будети ли вы дальше сражаться или добывать ресурсы в шахтах.", reply_markup=main_menu_keyboard())
        await state.clear()
