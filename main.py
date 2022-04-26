import asyncio
import os

from aiogram import Bot, Dispatcher, executor
from dotenv import load_dotenv

load_dotenv()
bot_token = os.getenv('TELEGRAM_TOKEN')
admin_id = os.getenv('ADMIN_ID')

loop = asyncio.get_event_loop()
bot = Bot(bot_token, parse_mode='HTML')
dp = Dispatcher(bot, loop=loop)

if __name__ == '__main__':
    from handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)
