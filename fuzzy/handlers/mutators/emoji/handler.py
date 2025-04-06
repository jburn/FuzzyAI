import logging

from typing import Any

from fuzzy.handlers.mutators.base import BaseMutator, mutators_fm
from fuzzy.handlers.mutators.enums import MutatorType

WORDS_TO_REPLACE = {
    "bomb": "💣",
    "explosive": "💣",
    "gun": "🔫",
    "pistol": "🔫",
    "weapon": "🔫",
    "knife": "🔪",
    "drug": "💊",
    "pill": "💊"
    }


logger = logging.getLogger(__name__)

@mutators_fm.flavor(MutatorType.EMOJI)
class EmojiMutator(BaseMutator):
    """
    A mutator that inserts emojis in the place of suspicious words
    """
    def __init__(self, **extra: Any):
        super().__init__(name=MutatorType.EMOJI, **extra)

    def __insert_emojis(self, string: str) -> str:
        for word, emoji in WORDS_TO_REPLACE.items():
            string = string.replace(word, emoji)
        return string

    async def mutate(self, prompt: str) -> str:
        logger.debug("Inserting emojis to prompt: %s", prompt)
        return self.__insert_emojis(prompt)
