from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.state import default_state

router = Router()


@router.message(default_state, Command("src"))
async def src(message: Message) -> None:
    await message.reply(
        "Исходный код <a href=\"https://github.com/mono245/TelegramRpsBot\">здесь</a>",
        parse_mode="HTML",
        disable_web_page_preview=True
    )
