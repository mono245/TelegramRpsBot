from time import strftime

from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters.command import Command

router = Router()


@router.message(Command("start"))
async def start(message: Message, bot: Bot) -> None:
    current = strftime("%Y-%m-%d -- %H:%M:%S")

    await message.answer(f"Bot started at {current}")
