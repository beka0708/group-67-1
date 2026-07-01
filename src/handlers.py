from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from src.keyboards import keyboard_main, inline

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! Я твой первый бот.", 
        reply_markup=inline
        )
    
    print(f"Пользователь {message.from_user.full_name}, его ID:{message.from_user.id}")


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(
        '/start - приветствие\n'
        '/help - список команд'
    )


@router.message(F.text == 'пока')
async def get_group(message: Message):
    await message.answer('Пока мой создатель!')



@router.message(F.text == 'Меню')
async def get_group(message: Message):
    await message.answer('Типа показываем меню...')


@router.message()
async def echo(message: Message):
    await message.answer(f"Ты написал {message.text}")
