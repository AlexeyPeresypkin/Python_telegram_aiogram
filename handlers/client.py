from aiogram import types, Dispatcher
from aiogram.utils.exceptions import BotBlocked

from create_bot import bot
from data_base.sqlite_db import sql_read
from keyboards import kb_client


# @dp.message_handler(commands=['start', 'help'])
async def commands_start(message: types.Message):
    try:
        await bot.send_message(
            message.from_user.id,
            'Приятного аппетита',
            reply_markup=kb_client
        )
        await message.delete()
    except BotBlocked:
        await message.reply(
            'Общение с ботом через ЛС, напишите ему:\n https://t.me/dialogs_flow_bot')


# @dp.message_handler(commands=['Режим работы'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        'Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00'
    )


# @dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Ул. Вкусная д.1')


async def pizza_menu_command(message: types.Message):
    await sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['Режим_работы'])
    dp.register_message_handler(pizza_place_command, commands=['Расположение'])
    dp.register_message_handler(pizza_menu_command, commands=['Меню'])
