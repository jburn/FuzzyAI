import logging
import random

from typing import Any
from string import punctuation, ascii_letters, digits, whitespace

from fuzzy.handlers.mutators.base import BaseMutator, mutators_fm
from fuzzy.handlers.mutators.enums import MutatorType


logger = logging.getLogger(__name__)

@mutators_fm.flavor(MutatorType.RANDADD_CHARACTER)
class RandaddCharacterMutator(BaseMutator):
    """
    A mutator that randomly adds 10% of the string length worth of characters into a prompt
    """
    def __init__(self, **extra: Any):
        super().__init__(name=MutatorType.RANDADD_CHARACTER, **extra)

    def __randadd_characters(self, string: str, ) -> str:
        output = ''
        for char in string:
            if random.random() < 0.1:
                output += random.choice(punctuation + ascii_letters + digits + whitespace)
            output += char
        return output

    async def mutate(self, prompt: str) -> str:
        logger.debug("Randomly adding characters to prompt: %s", prompt)
        return self.__randadd_characters(prompt)
