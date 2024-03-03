from random import choice as rchoice

from ..keyboards import main_kb
from ..utils import choices, is_player_win
from ..filters import RpsFilter

from aiogram import F, Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup, default_state
from aiogram.fsm.context import FSMContext

router = Router()


class InGame(StatesGroup):
    in_game = State()


@router.message(default_state, Command("play"))
async def play(message: Message, state: FSMContext) -> None:
    await state.update_data(choice=rchoice(choices))

    await message.answer(
        "Ваш ход:",
        reply_markup=main_kb()
    )
    await state.set_state(InGame.in_game)


@router.message(InGame.in_game, F.text, RpsFilter())
async def send_winner(message: Message, item: str, state: FSMContext) -> None:
    bot_data = await state.get_data()
    bot_choice = bot_data['choice']

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


# ----- cancel handlers -----
@router.message(default_state, Command("cancel"))
async def cancel_no_state(message: Message, state: FSMContext) -> None:
    await state.set_data({})
    await message.answer(
        "Нечего отменять",
        reply_markup=ReplyKeyboardRemove()
    )


@router.message(Command("cancel"))
async def cancel(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(
        "Игра отменена",
        reply_markup=ReplyKeyboardRemove()
    )
# ---------------------------


@router.message(InGame.in_game)
async def incorrect_input(message: Message, state: FSMContext) -> None:
    await message.answer(
        "Кажется, вы отправили что-то не то, "
        "пожалуйста выберите камень, ножницы или бумагу из списка ниже",
        reply_markup=main_kb()
    )
