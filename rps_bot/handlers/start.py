from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command

router = Router()


@router.message(Command("start"))
async def start(message: Message) -> None:
    await message.answer(
        "Привет, чтобы сыграть в камень, ножницы бумага отправь команду /play"
    )
