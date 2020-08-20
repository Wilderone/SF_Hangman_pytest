import pytest
import random
import string
from game_logic import Win_Lose
from words import _WORDS


test_symbols = list(''.join(random.SystemRandom().choice(
    string.ascii_lowercase + string.digits) for _ in range(20)))


@pytest.mark.parametrize('letter', test_symbols)
@pytest.mark.parametrize('word', _WORDS)
def test_letter_parametrized(letter, word):

    Win_Lose().check_letter(letter, word)
