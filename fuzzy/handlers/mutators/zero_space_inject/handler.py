import logging
import random

from typing import Any

from fuzzy.handlers.mutators.base import BaseMutator, mutators_fm
from fuzzy.handlers.mutators.enums import MutatorType


logger = logging.getLogger(__name__)

ZERO_SPACE_ASCII = ["\u200B", "\u200C", "\u200D"]

@mutators_fm.flavor(MutatorType.ZERO_SPACE_INJECT)
class ZeroSpaceCharacterMutator(BaseMutator):
    """
    A mutator that randomly adds 30% of the string length worth of zero-space ascii characters into a prompt
    """
    def __init__(self, **extra: Any):
        super().__init__(name=MutatorType.ZERO_SPACE_INJECT, **extra)

    def __randadd_characters(self, string: str, ) -> str:
        output = ''
        for char in string:
            if random.random() < 0.3:
                output += random.choice(ZERO_SPACE_ASCII)
            output += char
        return output

    async def mutate(self, prompt: str) -> str:
        logger.debug("Randomly adding zero-space ascii characters to prompt: %s", prompt)
        return self.__randadd_characters(prompt)
