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
dp = Dispatcher(bot=bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(texts.start, reply_markup=start_kb)

@dp.message_handler(text='Каталог')
async def price(message):
    await message.answer('Что Вас интересует?', reply_markup=catalog_kb)

@dp.message_handler(text='О нас...')
async def price(message):
    await message.answer(texts.about, reply_markup=start_kb)


@dp.message_handler(text='Сайт')
async def price(message):
    await message.answer('Перейти на сайт', reply_markup=site_kb)

@dp.callback_query_handler(text='small_game')
async def buy_small(call):
    await call.message.answer(texts.gameS, reply_markup=buy_kb)
    await call.answer()

@dp.callback_query_handler(text='medium_game')
async def buy_meduim(call):
    await call.message.answer(texts.gameM, reply_markup=buy_kb)
    await call.answer()

@dp.callback_query_handler(text='big_game')
async def buy_big(call):
    await call.message.answer(texts.gameL, reply_markup=buy_kb)
    await call.answer()

@dp.callback_query_handler(text='other')
async def buy_other(call):
    await call.message.answer(texts.other, reply_markup=buy_kb)
    await call.answer()

@dp.callback_query_handler(text='contact')
async def contact_me(call):
    await call.message.answer(texts.contact)
    await call.answer()

@dp.message_handler()
async def all_messages(message):
    await message.answer(texts.wrong_command)
    print(f'Получено: {message.text}')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)