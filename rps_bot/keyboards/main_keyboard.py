from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def main_kb() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    builder.button(text="Камень")
    builder.button(text="Ножницы")
    builder.button(text="Бумага")
    builder.adjust(2)

    return builder.as_markup(resize_keyboars=True, selective=True)
