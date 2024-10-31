from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Стоимость'),
            KeyboardButton(text='О нас...')
        ]
    ], resize_keyboard=True
)

catalog_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='0'),
            KeyboardButton(text='1')
        ]
    ], resize_keyboard=True
)