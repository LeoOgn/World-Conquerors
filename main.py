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
location_repository = LocationRepository(connection)
mob_repository = MobRepository(connection)
inventory_repository = InventoryRepository(connection)

user_service = UserService(user_repository)
character_service = CharacterService(character_repository)
location_service = LocationService(location_repository, mob_repository)
fight_service = FightService(mob_repository, character_repository)
inventory_service = InventoryService(inventory_repository)

start_handler = StartHandler(user_service, character_service)
location_handler = LocationHandler(location_service, fight_service)
fight_handler = FightHandler(fight_service, location_service, inventory_service)
character_handler = CharacterHandler(character_service)

command_router = CommandRouter(dp, start_handler)
location_router = LocationsRouter(dp, location_handler)
fight_router = FightsRouter(dp, fight_handler)
character_router = CharacterRouter(dp, character_handler)

async def start():
    await dp.start_polling(bot)

asyncio.run(start())