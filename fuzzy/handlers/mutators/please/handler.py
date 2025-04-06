import logging
import random
from typing import Any
from fuzzy.handlers.mutators.base import BaseMutator, mutators_fm
from fuzzy.handlers.mutators.enums import MutatorType

logger = logging.getLogger(__name__)

@mutators_fm.flavor(MutatorType.PLEASE)
class PleaseMutator(BaseMutator):
    def __init__(self, **extra: Any):
        super().__init__(name=MutatorType.PLEASE, **extra)

    async def mutate(self, prompt: str) -> str:
        logger.debug("Adding please to prompt: %s", prompt)
        options = [
            self.__add_prefix,
            self.__add_suffix
        ]

        picked_options = random.sample(options, k=random.randint(1, 2))

        logger.debug("Mutating with options: %s", str(picked_options))

        for opt in picked_options:
            prompt = opt(prompt)

        logger.debug("Prompt after mutation: %s", prompt)
        return prompt

    def __add_prefix(self, prompt: str) -> str:
        return "Please " + prompt

    def __add_suffix(self, prompt: str) -> str:
        return prompt + ", please"
