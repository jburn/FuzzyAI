import logging
from typing import Any

from fuzzy.handlers.mutators.base import BaseMutator, mutators_fm
from fuzzy.handlers.mutators.enums import MutatorType

logger = logging.getLogger(__name__)

@mutators_fm.flavor(MutatorType.BINARY_ENCODE)
class BinaryEncodeMutator(BaseMutator):
    """
    A mutator that applies binary encoding to the payload
    """
    def __init__(self, **extra: Any):
        super().__init__(name=MutatorType.BINARY_ENCODE, **extra)

    def __binary_encode(self, string: str) -> str:
        return ' '.join(format(ord(char), 'b') for char in string)

    async def mutate(self, prompt: str) -> str:
        logger.debug("Encoding prompt with binary encoding: %s", prompt)
        return self.__binary_encode(prompt)
