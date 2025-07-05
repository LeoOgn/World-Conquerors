from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from sqlite3 import connect
import os, asyncio

from repositories import *
from services import *
from handlers import *
from routers import *


load_dotenv(override=True)
bot = Bot(os.getenv("TOKEN"))
dp = Dispatcher()

connection = connect("db.db")
user_repository = UserRepository(connection)
character_repository = CharacterRepository(connection)
user_service = UserService(user_repository)
character_service = CharacterService(character_repository)
start_handler = StartHandler(user_service, character_service)
command_router = CommandRouter(dp, start_handler)

async def start():
    await dp.start_polling(bot)

asyncio.run(start())