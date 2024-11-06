from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Каталог'),
            KeyboardButton(text='О нас...'),
            KeyboardButton(text='Сайт')
        ]
    ], resize_keyboard=True
)

catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Малая игра', callback_data='small_game')],
        [InlineKeyboardButton(text='Средняя игра', callback_data='medium_game')],
        [InlineKeyboardButton(text='Большая игра', callback_data='big_game')],
        [InlineKeyboardButton(text='Другие предложения', callback_data='other')],
        [InlineKeyboardButton(text='Контакты', callback_data='contact')]
    ], resize_keyboard=True
)

buy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Купить!', url='https://www.ozon.ru/category/nastolnye-i-kartochnye-igry-13506/')],
        [InlineKeyboardButton(text='Назад', callback_data='back_to_catalog')]
    ]
)

site_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Да', url='https://tsukanov-lab.moy.su/index/tsukanov_lab/0-2')]
    ]
)

admin_panel_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Пользователи', callback_data='users')],
        [InlineKeyboardButton(text='Статистика', callback_data='stat')],
        [
            InlineKeyboardButton(text='Блокировка', callback_data='block'),
            InlineKeyboardButton(text='Разблокировка', callback_data='unblock')
        ]
    ]

)