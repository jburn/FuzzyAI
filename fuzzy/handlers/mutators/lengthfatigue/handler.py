import logging
import random

from typing import Any

from fuzzy.handlers.mutators.base import BaseMutator, mutators_fm
from fuzzy.handlers.mutators.enums import MutatorType


logger = logging.getLogger(__name__)

@mutators_fm.flavor(MutatorType.LENGTHFATIGUE)
class LengthfatigueMutator(BaseMutator):
    """
    A mutator that makes the prompt repeat 10-100 times
    """
    def __init__(self, **extra: Any):
        super().__init__(name=MutatorType.EMOJI, **extra)

    def __multiply_prompt(self, string: str) -> str:
        return " ".join([string] * random.randint(10, 100))

    async def mutate(self, prompt: str) -> str:
        logger.debug("Multiplying prompt: %s", prompt)
        return self.__multiply_prompt(prompt)
