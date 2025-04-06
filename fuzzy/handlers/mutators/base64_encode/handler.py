import logging
import base64
from typing import Any

from fuzzy.handlers.mutators.base import BaseMutator, mutators_fm
from fuzzy.handlers.mutators.enums import MutatorType

logger = logging.getLogger(__name__)

@mutators_fm.flavor(MutatorType.BASE64_ENCODE)
class Base64EncodeMutator(BaseMutator):
    """
    A mutator that base64 encodes the input
    """
    def __init__(self, **extra: Any):
        super().__init__(name=MutatorType.BASE64_ENCODE, **extra)

    def __base64_encode(self, string: str) -> str:
        return str(base64.b64encode(string.encode("utf-8")).decode("utf-8"))

    async def mutate(self, prompt: str) -> str:
        logger.debug("Encoding prompt with base64: %s", prompt)
        return self.__base64_encode(prompt)
