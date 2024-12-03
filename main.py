from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "7890890424:AAEwL3AvXADeymJq1hsVzEH_kAkWYnGdBsc"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


# @dp.message_handler()
# async def all_message(message):
#     print("Мы получили сообщение!")


@dp.message_handler(text=['Urban', 'ff'])
async def urban_message(message):
    print('Urban message')


if __name__ == "__main_":
    executor.start_polling(dp, skip_updates=True)
