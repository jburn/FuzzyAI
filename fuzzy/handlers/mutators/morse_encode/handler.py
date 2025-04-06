import logging
from typing import Any

from fuzzy.handlers.mutators.base import BaseMutator, mutators_fm
from fuzzy.handlers.mutators.enums import MutatorType

MORSE_CHAR = {
    'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-',"Á": ".--.-",
    "À": ".--.-", "Â": ".-..-.","Ã": ".--.-",
    "Ä": ".-.-","Å": ".--.-","Ç": "-.-..",
    "É": "..-..","È": "..-..","Ê": ".-..-.",
    "Ë": "..-..","Í": "..--.","Ì": "..--.",
    "Î": "..-..","Ï": "..--.","Ñ": "--.--",
    "Ó": "---.","Ò": "---.","Ô": "---.",
    "Õ": "---.","Ö": "---.","Ú": "..--",
    "Ù": "..--","Û": "..--","Ü": "..--"
    }
logger = logging.getLogger(__name__)

@mutators_fm.flavor(MutatorType.MORSE_ENCODE)
class MorseEncodeMutator(BaseMutator):
    """
    A mutator that applies morse encoding to the payload
    """
    def __init__(self, **extra: Any):
        super().__init__(name=MutatorType.MORSE_ENCODE, **extra)

    def __morse_encode(self, string: str) -> str:
        return ''.join(MORSE_CHAR[char] if char in MORSE_CHAR else '' for char in string)

    async def mutate(self, prompt: str) -> str:
        logger.debug("Encoding prompt with morse encoding: %s", prompt)
        return self.__morse_encode(prompt)
