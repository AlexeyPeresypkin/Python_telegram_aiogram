import os

from aiogram import Bot, Dispatcher, executor
from dotenv import load_dotenv
from aiogram.contrib.fsm_storage.memory import MemoryStorage

load_dotenv()
bot_token = os.getenv('TELEGRAM_TOKEN')
admin_id = os.getenv('ADMIN_ID')

storage = MemoryStorage()

bot = Bot(bot_token)
dp = Dispatcher(bot, storage=storage)
