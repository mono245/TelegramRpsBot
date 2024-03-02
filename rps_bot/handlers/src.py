from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command("src"))
async def src(message: Message) -> None:
    await message.reply(
        "Исходный код <a href=\"https://github.com/mono245/TelegramRpsBot\">здесь</a>",
        parse_mode="HTML",
        disable_web_page_preview=True
    )
