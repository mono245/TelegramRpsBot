from random import choice

from ..keyboards import main_kb
from ..utils import choices, is_player_win
from ..filters import RpsFilter

from aiogram import F, Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command, StateFilter
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

router = Router()
bot_choice = None


class InGame(StatesGroup):
    in_game = State()


@router.message(Command("play"))
async def play(message: Message, state: FSMContext) -> None:
    global bot_choice
    bot_choice = choice(choices)

    await message.answer(
        "Ваш ход:",
        reply_markup=main_kb()
    )
    await state.set_state(InGame.in_game)


@router.message(InGame.in_game, F.text, RpsFilter())
async def send_winner(message: Message, item: str, state: FSMContext):
    status = is_player_win(bot_choice, item)
    match status:
        case True:
            msg = "Вы победили!"
        case False:
            msg = "Вы проиграли!"
        case "tie":
            msg = "Ничья!"
    await message.answer(
        f"Мой ход: {bot_choice}",
        reply_markup=ReplyKeyboardRemove()
    )

    await message.answer(
        f"Бот: {bot_choice}\nВы: {item}\n{msg}\n"
        "Если хотите сыграть еще, отправьте боту /play",
    )
    await state.clear()


@router.message(InGame.in_game)
async def incorrect_input(message: Message, state: FSMContext):
    await message.answer(
        "Кажется, вы отправили что-то не то, "
        "пожалуйста выберите камень, ножницы или бумагу из списка ниже",
        reply_markup=main_kb()
    )
