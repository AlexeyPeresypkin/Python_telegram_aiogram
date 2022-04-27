import asyncio
import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.exceptions import BotBlocked
from dotenv import load_dotenv

load_dotenv()
bot_token = os.getenv('TELEGRAM_TOKEN')
admin_id = os.getenv('ADMIN_ID')

loop = asyncio.get_event_loop()
bot = Bot(bot_token)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Bot is online')

@dp.message_handler(commands=['start', 'help'])
async def commands_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита')
        await message.delete()
    except BotBlocked:
        await message.reply(
            'Общение с ботом через ЛС, напишите ему:\n https://t.me/dialogs_flow_bot')


@dp.message_handler(commands=['Режим работы'])
async def pizza_opne_command(message: types.Message):
    await bot.send_message((message.from_user.id,
                            'Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00'))


@dp.message_handler(commands=['Расположение'])
async def pizza_opne_command(message: types.Message):
    await bot.send_message((message.from_user.id, 'Ул. Вкусная д.1'))


@dp.message_handler()
async def echo_send(message: types.Message):
    await message.answer(message.text)
    # await message.reply(message.text)
    # await bot.send_message(message.from_user.id, message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
