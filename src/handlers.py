from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from src.questions import QUESTIONS
from src.keyboards import keyboard_main, inline
from db.users import create_user, get_user

router = Router()


class Quiz(StatesGroup):
    waiting_answer = State()



@router.message(CommandStart())
async def cmd_start(message: Message):
    user = create_user(
        telegram_id=message.from_user.id,
        username=message.from_user.username or "Аноним"
    )
    await message.answer(
        f"Привет, {message.from_user.first_name}! Я твой первый бот.\n {user}"
        )
    
    print(f"Пользователь {message.from_user.full_name}, его ID:{message.from_user.id}")


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(
        '/start - приветствие\n'
        '/help - список команд'
    )


@router.message(Command('game'))
async def cmd_game(message: Message):
    await message.answer("Выбери один из пунктов", reply_markup=inline)


@router.message(F.text == 'пока')
async def get_group(message: Message):
    await message.answer('Пока мой создатель!')



@router.message(F.text == 'Меню')
async def get_group(message: Message):
    await message.answer('Типа показываем меню...')



@router.callback_query(F.data == 'quiz_start')
async def start_quiz(callback: CallbackQuery, state: FSMContext):
    await callback.answer('Начинаем игру!!!', show_alert=True)
    await state.update_data(index=0, score=0)
    await state.set_state(Quiz.waiting_answer)
    await callback.message.answer(f"Вопрос 1: {QUESTIONS[0]['q']}")



# Хендлер - сработает ТОЛЬКО в состоянии waitinf_answer
@router.message(Quiz.waiting_answer)  
async def handle_answer(message: Message, state: FSMContext):
    data = await state.get_data()
    index = data['index']
    score = data['score']

    if message.text.lower() == QUESTIONS[index]['a']:
        score += 1
        await message.answer("Правильно! +1")
    else:
        await message.answer(f"Неправильно. Правильный ответ: {QUESTIONS[index]['a']}")
    
    index += 1

    if index >= len(QUESTIONS):
        await message.answer(f"Конец! Счет: {score}/{len(QUESTIONS)}")
        await state.clear()
    else:
        await state.update_data(index=index, score=score)
        await message.answer(f"Вопрос {index+1}: {QUESTIONS[index]['q']}")


# FSM - Finite State Machine