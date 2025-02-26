import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.amswer("Hello This is your first bot !!!")


@dp.message(Command("help"))
async def help_(message: types.Message):
    await message.answer("You asked help?")

@dp.message()
async def echo(message: types.Message):
    if message.text == "potato":
        await message.answer("Ты потато)")
    elif message.text == "apple" or message.text == "orange":
        await message.answer("А это вкусные фрукты")
    else:
        await message.answer(f"You typed {message.text}")


async def main():
    print("Bot started...")
    await dp.start_polling(bot)


if __name__== '__main__':
    asyncio.run(main())
    ##