import logging
import random

from typing import Any
from string import punctuation

from fuzzy.handlers.mutators.base import BaseMutator, mutators_fm
from fuzzy.handlers.mutators.enums import MutatorType


logger = logging.getLogger(__name__)

@mutators_fm.flavor(MutatorType.PUNCTUATIONSPAM)
class PunctuationspamMutator(BaseMutator):
    """
    A mutator that multiplies punctuation characters in a string
    """
    def __init__(self, **extra: Any):
        super().__init__(name=MutatorType.PUNCTUATIONSPAM, **extra)

    def __multiply_punctuation(self, string: str) -> str:
        return "".join([char * random.randint(2, 10) if char in punctuation else char for char in string])

    async def mutate(self, prompt: str) -> str:
        logger.debug("Multiply punctuation characters in prompt: %s", prompt)
        return self.__multiply_punctuation(prompt)
