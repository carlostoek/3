from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from .config import Settings

bot = Bot(token=Settings().BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)