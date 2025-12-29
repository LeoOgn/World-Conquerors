from handlers.character_handler import CharacterHandler
from handlers.location_handler import LocationHandler
from services import UserService, CharacterService
from keyboards import MainMenuCallback, inline_main_menu_keyboard
from aiogram import types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


class CreateCharacterState(StatesGroup):
    name = State()


class StartHandler:
    def __init__(
            self, 
            user_service: UserService,
            character_service: CharacterService,
            character_handler: CharacterHandler,
            location_handler: LocationHandler
        ):
        self.user_service = user_service
        self.character_service = character_service
        self.character_handler = character_handler
        self.location_handler = location_handler

    async def start_command(self, msg: types.Message, state: FSMContext):
        if not self.user_service.check_auth(msg.from_user.id):
            self.user_service.signup(msg.from_user.id, msg.from_user.username)
            await msg.answer("Здравствуй путник! Как зовут тебя?")
            await state.set_state(CreateCharacterState.name)
        else:
            await msg.answer_photo(
                photo=types.FSInputFile("images/Город-столица.jpg"), 
                caption=f"Здравствуй путник! Лор", 
                reply_markup=inline_main_menu_keyboard()
            )

    async def handle(self, callback: types.CallbackQuery, callback_data: MainMenuCallback):
        match callback_data.action:
            case "character":
                await self.character_handler.inline_character_handler(callback)
            case "wasteland":
                await self.location_handler.inline_location_menu(callback)

    async def get_character_name(self, msg: types.Message, state: FSMContext):
        name = msg.text
        self.character_service.create_character(name, msg.from_user.id)
        await msg.answer("Поздравляем! Вы создали своего персонажа! Теперь только вам решать, будети ли вы дальше сражаться или добывать ресурсы в шахтах. Но для начала вам следует зайти во вкладку \"Персонаж 🧔🏻‍♀️\", \"Повысить характеристики\"", reply_markup=inline_main_menu_keyboard())
        await state.clear()
