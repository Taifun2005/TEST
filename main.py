from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio

api = "7890890424:AAEwL3AvXADeymJq1hsVzEH_kAkWYnGdBsc"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = InlineKeyboardButton()
button1 = InlineKeyboardButton(text='Информация', callback_data='info')

kb.add(button1)

# stat_menu = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text='info')],
#         [
#             KeyboardButton(text="shop"),
#             KeyboardButton(text='donate')
#         ]
#     ], resize_keyboard=True
# )


@dp.message_handler(commands=['start'])
async def starter(message):
    await message.answer("Рады вас видеть", reply_markup=kb)


@dp.callback_query_handler(text = 'info')
async def infor(call):
    await call.message.answer("Информация о боте")
    await  call.answer()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)