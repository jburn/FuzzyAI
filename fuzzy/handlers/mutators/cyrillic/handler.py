import logging

from typing import Any

from fuzzy.handlers.mutators.base import BaseMutator, mutators_fm
from fuzzy.handlers.mutators.enums import MutatorType

CYRILLIC_LOOKALIKES = {
    "a": "а",
    "e": "е",
    "i": "і",
    "o": "о",
    "c": "с"
    }

logger = logging.getLogger(__name__)

@mutators_fm.flavor(MutatorType.CYRILLIC)
class CyrillicMutator(BaseMutator):
    """
    A mutator that replaces latin letters with similiar cyrillic letters
    """
    def __init__(self, **extra: Any):
        super().__init__(name=MutatorType.CYRILLIC, **extra)

    def __insert_cyrillic(self, string: str) -> str:
        for char, cyrillic in CYRILLIC_LOOKALIKES.items():
            string = string.replace(char, cyrillic)
        return string

    async def mutate(self, prompt: str) -> str:
        logger.debug("Inserting cyrillic letters to prompt: %s", prompt)
        return self.__insert_cyrillic(prompt)
