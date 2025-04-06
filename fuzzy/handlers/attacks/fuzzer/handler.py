import logging
import random
import time
import inspect

from pydantic import BaseModel, Field

from typing import Any, Optional, Type
from fuzzy.consts import DEFAULT_OPEN_SOURCE_MODEL
from fuzzy.handlers.mutators.base import BaseMutator
from fuzzy.handlers.mutators import (
    MorseEncodeMutator,
    Base64EncodeMutator,
    BinaryEncodeMutator,
    RandropMutator,
    RephraseMutator,
    SummarizeMutator,
    PleaseMutator,
    TranslateDutchMutator,
    TranslateFrenchMutator,
    TranslateGermanMutator,
    TranslateItalianMutator,
    TranslatePortugeseMutator,
    TranslateSpanishMutator,
    CaseShuffleMutator,
    CyrillicMutator,
    EmojiMutator,
    HomophoneMutator,
    LeetspeakMutator,
    LengthfatigueMutator,
    PunctuationspamMutator,
    RandaddCharacterMutator,
    RandropCharacterMutator,
    RepetitionMutator,
    SynonymMutator,
    ZeroSpaceCharacterMutator,
    TranslateMutator
)
from fuzzy.handlers.attacks.base import (
    BaseAttackTechniqueHandler,
    BaseAttackTechniqueHandlerException,
    attack_handler_fm)
from fuzzy.handlers.attacks.fuzzer.prompt_templates import (
    ATTACKING_PROMPTS_TEMPLATES, CROSSOVER_ACTION_PROMPT,
    EXPAND_ACTION_PROMPT, GENERATE_ACTION_PROMPT,
    REPHRASE_ACTION_PROMPT, SHORTEN_ACTION_PROMPT)
from fuzzy.handlers.attacks.enums import FuzzerAttackMode
from fuzzy.handlers.attacks.models import AttackResultEntry
from fuzzy.llm.providers.base import BaseLLMProvider

logger = logging.getLogger(__name__)

MUTATOR_TYPES = [
    RephraseMutator,
    SummarizeMutator,
    PleaseMutator,
    HomophoneMutator,
    SynonymMutator,
    EmojiMutator,
    #TranslateDutchMutator,
    #TranslateFrenchMutator,
    #TranslateGermanMutator,
    #TranslateItalianMutator,
    #TranslatePortugeseMutator,
    #TranslateSpanishMutator,
    RandropMutator,
    CaseShuffleMutator,
    CyrillicMutator,
    LeetspeakMutator,
    LengthfatigueMutator,
    PunctuationspamMutator,
    RandaddCharacterMutator,
    RandropCharacterMutator,
    RepetitionMutator,
    ZeroSpaceCharacterMutator,
    #MorseEncodeMutator,
    #Base64EncodeMutator,
    #BinaryEncodeMutator,
]

DEFAULT_TRANSLATION_MODEL = "ollama/thinkverse/towerinstruct"

class FuzzerAttackHandlerExtraParams(BaseModel):
    reps: int = Field(1, description=f"Number of attempted attacks for each supplied prompt. Default: 1")
    mutation_model: str = Field(DEFAULT_OPEN_SOURCE_MODEL,
                                description=f"Use a different model than the target model to mutate prompt (default: {DEFAULT_OPEN_SOURCE_MODEL})")
    translation_model: str = Field(DEFAULT_TRANSLATION_MODEL,
                                   description=f"Use a different model than the default model to translate prompt (default: {DEFAULT_TRANSLATION_MODEL})")

@attack_handler_fm.flavor(FuzzerAttackMode.FUZZER)
class FuzzerAttackHandler(BaseAttackTechniqueHandler[FuzzerAttackHandlerExtraParams]):
    def __init__(self, **extra: Any):
        super().__init__(**extra)
        if self._extra_args.mutation_model not in self._model_queue_map:
            raise RuntimeError(f"Mutation model: {self._extra_args.mutation_model} was not added to the fuzzer,"
                               " please make sure you add it with -x <provider/model> and set"
                               " -e mutation_model=<provider/model> accordingly.")

        if self._extra_args.translation_model not in self._model_queue_map:
            raise RuntimeError(f"Translation model: {self._extra_args.translation_model} was not added to the fuzzer,"
                               " please make sure you add it with -x <provider/model> and set"
                               " -e translation_model=<provider/model> accordingly.")

    async def _attack(self, prompt: str, **extra: Any) -> Optional[AttackResultEntry]:
        llm: BaseLLMProvider
        async with self._borrow(self._model) as llm:
            random.seed(time.time_ns()) # pseudorandom seed
            attack_prompt = prompt
            chosen_mutators = random.choices(MUTATOR_TYPES, k=random.randint(2, 4))
            logging.info(chosen_mutators)
            for mutator_type in chosen_mutators:
                if issubclass(mutator_type, TranslateMutator):
                    async with self._borrow(self._extra_args.translation_model) as translation_model:
                        #logging.info("%s", translation_model)
                        mutator = mutator_type(translation_model)
                elif 'llm' in inspect.signature(mutator_type).parameters:
                    async with self._borrow(self._extra_args.mutation_model) as mutation_model:
                        #logging.info("%s", mutation_model)
                        mutator = mutator_type(mutation_model)
                else:
                    mutator = mutator_type()
                attack_prompt = await mutator.mutate(prompt=attack_prompt)
            response = await llm.generate(attack_prompt, **self._extra)
            result = AttackResultEntry(original_prompt=prompt,
                                       current_prompt=attack_prompt,
                                       response=response.response) if response else None
            logger.debug("Response: %s", response.response if response else "None")

        classifications = await self._classify_llm_response(response, original_prompt=prompt)

        if result:
            result.classifications = classifications

        return result

    @classmethod
    def extra_args_cls(cls) -> Type[BaseModel]:
        return FuzzerAttackHandlerExtraParams
