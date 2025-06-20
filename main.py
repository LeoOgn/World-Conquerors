from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import load_dotenv
import os, asyncio


load_dotenv(override=True)
bot = Bot(os.getenv("TOKEN"))
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(msg: types.Message):
    print(msg.from_user.username, msg.from_user.full_name, msg.from_user.id)
    await msg.answer("Привет добытчик! Назовись для учета!")

async def start():
    await dp.start_polling(bot)

asyncio.run(start())