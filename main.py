from data_base import db_start, creat_users_id
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from constants import HELP_COMMAND, API_TOKEN, admin_ids
from filters import IsAdmin


bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

@dp.message(Command(commands=['start']))
async def start_message(message: Message):
    db_start()
    await message.answer(creat_users_id(message.from_user.id),
                         parse_mode='HTML')

# Нужно создать вторую таблицу со списком контактов и связать с юзер id

@dp.message(Command(commands=['help']))
async def help_command(message: Message):
    await message.answer(HELP_COMMAND,
                         parse_mode='HTML')



if __name__ == '__main__':
    dp.run_polling(bot)

# ПРОВЕРЯЕТ ПОЛЬЗОВАТЕЛЬ АДМИН ИЛИ НЕТ
# @dp.message(IsAdmin(admin_ids))
# async def answer_if_admins_update(message: Message):
#     await message.answer(text='Вы админ')
