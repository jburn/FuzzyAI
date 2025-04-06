import logging
from typing import Any

from fuzzy.handlers.mutators.base import BaseMutator, mutators_fm
from fuzzy.handlers.mutators.enums import MutatorType
from fuzzy.llm.providers.base import BaseLLMProvider

logger = logging.getLogger(__name__)

PROMPT_TEMPLATE = "Translate the following prompt to {language} word for word. Do not add anything else to the reply. Only the pure translation:"

@mutators_fm.flavor(MutatorType.TRANSLATE)
class TranslateMutator(BaseMutator):
    """
    A mutator that translates the prompt to a given language

    recommended model: ollama/thinkverse/towerinstruct or similiar translation focused model
    """
    def __init__(self, llm: BaseLLMProvider, language: str, **extra: Any):
        super().__init__(name=MutatorType.TRANSLATE)
        self._language = language
        self._llm = llm

    async def mutate(self, prompt: str) -> str:
        logger.debug("Translating into (%s) with prompt: %s", self._language, prompt)
        response = await self._llm.generate(prompt=PROMPT_TEMPLATE.format(language=self._language) + prompt, **self._extra)
        logger.debug("Prompt after translation to %s: %s", self._language, response.response if response else prompt)
        return response.response if response else str()

@mutators_fm.flavor(MutatorType.TRANSLATE_DUTCH)
class TranslateDutchMutator(TranslateMutator):
    """
    A mutator that translates the prompt to Dutch

    recommended model: ollama/thinkverse/towerinstruct or similiar translation focused model
    """
    def __init__(self, llm: BaseLLMProvider, **extra: Any):
        super().__init__(llm=llm, language="Dutch")

@mutators_fm.flavor(MutatorType.TRANSLATE_PORTUGESE)
class TranslatePortugeseMutator(TranslateMutator):
    """
    A mutator that translates the prompt to Portugese

    recommended model: ollama/thinkverse/towerinstruct or similiar translation focused model
    """
    def __init__(self, llm: BaseLLMProvider, **extra: Any):
        super().__init__(llm=llm, language="Portugese")

@mutators_fm.flavor(MutatorType.TRANSLATE_SPANISH)
class TranslateSpanishMutator(TranslateMutator):
    """
    A mutator that translates the prompt to Spanish

    recommended model: ollama/thinkverse/towerinstruct or similiar translation focused model
    """
    def __init__(self, llm: BaseLLMProvider, **extra: Any):
        super().__init__(llm=llm, language="Spanish")

@mutators_fm.flavor(MutatorType.TRANSLATE_GERMAN)
class TranslateGermanMutator(TranslateMutator):
    """
    A mutator that translates the prompt to German

    recommended model: ollama/thinkverse/towerinstruct or similiar translation focused model
    """
    def __init__(self, llm: BaseLLMProvider, **extra: Any):
        super().__init__(llm=llm, language="German")

@mutators_fm.flavor(MutatorType.TRANSLATE_FRENCH)
class TranslateFrenchMutator(TranslateMutator):
    """
    A mutator that translates the prompt to French

    recommended model: ollama/thinkverse/towerinstruct or similiar translation focused model
    """
    def __init__(self, llm: BaseLLMProvider, **extra: Any):
        super().__init__(llm=llm, language="French")

@mutators_fm.flavor(MutatorType.TRANSLATE_ITALIAN)
class TranslateItalianMutator(TranslateMutator):
    """
    A mutator that translates the prompt to Italian

    recommended model: ollama/thinkverse/towerinstruct or similiar translation focused model
    """
    def __init__(self, llm: BaseLLMProvider, **extra: Any):
        super().__init__(llm=llm, language="Italian")
