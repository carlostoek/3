from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message
import asyncio

from config import BOT_TOKEN
from handlers.start_handler import start_handler

async def main():
    # Inicializa el bot y el despachador
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Registra el manejador para el comando /start
    dp.message.register(start_handler, CommandStart())

    # Inicia el bot
    try:
        await dp.start_polling(bot)
    finally:
        await bot.close()

if __name__ == '__main__':
    asyncio.run(main())