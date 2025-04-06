import logging
import random

from typing import Any

from fuzzy.handlers.mutators.base import BaseMutator, mutators_fm
from fuzzy.handlers.mutators.enums import MutatorType


logger = logging.getLogger(__name__)

@mutators_fm.flavor(MutatorType.REPETITION)
class RepetitionMutator(BaseMutator):
    """
    A mutator that randomly repeats each word in a prompt 1-6 times
    """
    def __init__(self, **extra: Any):
        super().__init__(name=MutatorType.REPETITION, **extra)

    def __add_repetition(self, string: str, ) -> str:
        words = string.split()
        return " ".join(" ".join([word] * random.randint(1, 6)) for word in words)

    async def mutate(self, prompt: str) -> str:
        logger.debug("Randomly adding word repetition to prompt: %s", prompt)
        return self.__add_repetition(prompt)
