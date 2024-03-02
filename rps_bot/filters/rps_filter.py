from typing import Any
from aiogram.filters import BaseFilter
from aiogram.types import Message

from ..utils.decide_winner import choices


class RpsFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool | dict[str, str]:
        if message.text.lower() in choices:
            return {"item": message.text.lower()}
        
        return False
