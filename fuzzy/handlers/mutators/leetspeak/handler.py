import logging
import random

from typing import Any

from fuzzy.handlers.mutators.base import BaseMutator, mutators_fm
from fuzzy.handlers.mutators.enums import MutatorType

ALL_LEET_CHARACTERS = {
    'a': ['4'],
    'b': ['8'],
    'c': ['<', '['],
    'd': ['|)'],
    'e': ['3', '€', '£'],
    'f': ['|='],
    'g': ['6'],
    'h': ['#'],
    'i': ['1', '|'],
    'j': [']'],
    'k': ['|<'],
    'l': ['1'],
    'm': ['|V|'],
    'n': ['|\\|'],
    'o': ['0'],
    'p': ['0_'],
    'q': ['(,)'],
    'r': ['|2'],
    's': ['5'],
    't': ['7'],
    'u': ['(_)'],
    'v': ['\\/'],
    'w': ['\\/\\/'],
    'x': ['><'],
    'y': ['`/'],
    'z': ['2']
    }

# clearer leet symbols for more understandable text
RELAXED_LEET_CHARACTERS = {
    'a': ['4'],
    'b': ['8'],
    'e': ['3'],
    'g': ['6'],
    'i': ['1'],
    'l': ['1'],
    'o': ['0'],
    's': ['5'],
    't': ['7'],
    'z': ['2']
}


logger = logging.getLogger(__name__)

@mutators_fm.flavor(MutatorType.LEETSPEAK)
class LeetspeakMutator(BaseMutator):
    """
    A mutator that translates roughly half the characters
    in the payload into leetspeak (replace characters with lookalikes)
    """
    def __init__(self, **extra: Any):
        super().__init__(name=MutatorType.LEETSPEAK, **extra)

    def __translate_to_leetspeak(self, string: str, relaxed=True) -> str:
        output = ''
        for char in string:
            LEET_CHARACTERS = RELAXED_LEET_CHARACTERS if relaxed else ALL_LEET_CHARACTERS
            if char in LEET_CHARACTERS and (random.random() < 0.5):
                output += random.choice(LEET_CHARACTERS[char.lower()])
            else:
                output += char
        return output

    async def mutate(self, prompt: str) -> str:
        logger.debug("Translating prompt to leetspeak: %s", prompt)
        return self.__translate_to_leetspeak(prompt)
