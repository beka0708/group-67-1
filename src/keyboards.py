from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton,
                           InlineKeyboardButton,
                           InlineKeyboardMarkup)


keyboard_main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Каталог")],
    [KeyboardButton(text="Меню"), KeyboardButton(text="Профиль")]
], resize_keyboard=True, input_field_placeholder="Выберите один пункт")


inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Начать викторину", callback_data="quiz_start")],
    [InlineKeyboardButton(text="Мой счет", callback_data="my_score")],
    [InlineKeyboardButton(text="Наш сайт", url="https://geeks.kg", callback_data="geeks")]
])