from typing import Literal

choices = ("камень", "ножницы", "бумага")


def is_player_win(
    bot: Literal["камень", "ножницы", "бумага"],
    player: Literal["камень", "ножницы", "бумага"]
    ) -> bool | str:
    """
    Returns True, if the player wins, else False
    Returns "tie", if its tie
    """
    bot, player = bot.lower(), player.lower()

    if player not in choices:
        raise ValueError("Invalid value, must be камень, ножницы or бумага")

    if bot == player:
        return "tie"

    match bot:
        case "камень":
            return player == "бумага"
        case "бумага":
            return player == "ножницы"
        case "ножницы":
            return player == "камень"
