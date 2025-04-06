import logging
import random

from typing import Any

from fuzzy.handlers.mutators.base import BaseMutator, mutators_fm
from fuzzy.handlers.mutators.enums import MutatorType


logger = logging.getLogger(__name__)

@mutators_fm.flavor(MutatorType.CASE_SHUFFLE)
class CaseShuffleMutator(BaseMutator):
    """
    A mutator that changes the case of characters in a string
    """
    def __init__(self, **extra: Any):
        super().__init__(name=MutatorType.CASE_SHUFFLE, **extra)

    def __shuffle_character_case(self, string: str) -> str:
        return "".join([char.lower() if random.random() < 0.5 else char.upper() for char in string])

    async def mutate(self, prompt: str) -> str:
        logger.debug("Randomly changing case of characters in prompt: %s", prompt)
        return self.__shuffle_character_case(prompt)
