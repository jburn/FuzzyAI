import logging
import random

from typing import Any

from fuzzy.handlers.mutators.base import BaseMutator, mutators_fm
from fuzzy.handlers.mutators.enums import MutatorType


logger = logging.getLogger(__name__)

@mutators_fm.flavor(MutatorType.RANDROP_CHARACTER)
class RandropCharacterMutator(BaseMutator):
    """
    A mutator that randomly drops 10% of the characters in a prompt
    """
    def __init__(self, **extra: Any):
        super().__init__(name=MutatorType.RANDROP_CHARACTER, **extra)

    def __randrop_characters(self, string: str) -> str:
        return "".join([char if random.random() < 0.9 else '' for char in string])

    async def mutate(self, prompt: str) -> str:
        logger.debug("Randomly dropping characters from prompt: %s", prompt)
        return self.__randrop_characters(prompt)
