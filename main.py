# ставим python 3.9
# ставим aiogram 2.25.1

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
#from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
#from aiogram.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import asyncio
import logging

from config import *
from keyboards import *
import texts

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(command=['start'])
async def start(message):
    await message.answer(texts.start, reply_markup=start_kb)

@dp.message_handler(text='О нас...')
async def price(message):
    await message.answer(texts.about, reply_markup=start_kb)

@dp.message_handler(text='Стоимость')
async def price(message):
    await message.answer('Что Вас интересует?', reply_markup=catalog_kb)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)