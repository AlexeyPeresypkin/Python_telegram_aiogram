import os

from aiogram import Bot, Dispatcher, executor
from dotenv import load_dotenv

load_dotenv()
bot_token = os.getenv('TELEGRAM_TOKEN')
admin_id = os.getenv('ADMIN_ID')
bot = Bot(bot_token)
dp = Dispatcher(bot)
