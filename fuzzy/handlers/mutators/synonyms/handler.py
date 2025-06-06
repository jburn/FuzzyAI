import logging
from typing import Any

from fuzzy.handlers.mutators.base import BaseMutator, mutators_fm
from fuzzy.handlers.mutators.enums import MutatorType
from fuzzy.llm.providers.base import BaseLLMProvider

logger = logging.getLogger(__name__)

PROMPT_TEMPLATE = "Replace all suitable words in the following prompt with synonyms. Do not add anything else to the reply. Only the pure converted prompt:"

@mutators_fm.flavor(MutatorType.SYNONYM)
class SynonymMutator(BaseMutator):
    """
    A mutator that replaces words in a prompt with synonyms
    """
    def __init__(self, llm: BaseLLMProvider, **extra: Any):
        super().__init__(name=MutatorType.SYNONYM)
        self._llm = llm

    async def mutate(self, prompt: str) -> str:
        logger.debug("Inserting synonyms to prompt: %s", prompt)
        response = await self._llm.generate(prompt=PROMPT_TEMPLATE + prompt, **self._extra)
        logger.debug("Response to synonym-injected prompt: %s", response.response if response else prompt)
        return response.response if response else str()
