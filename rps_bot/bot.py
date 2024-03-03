import asyncio
import logging
import os

from .handlers import play, src, start

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s |%(levelname)s| - %(name)s: %(message)s"
    )
    load_dotenv()

    bot = Bot(os.getenv("BOT_TOKEN"))
    dp = Dispatcher()
    dp.include_routers(play.router, src.router, start.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
