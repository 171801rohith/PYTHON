from cards_proj.src.cards import Card
import pytest

def test_equality_fail():
    c1 = Card("sit there", "brain")
    c2 = Card("do something", "nihir")
    # assert c1 == c2
    if c1 != c2:
        pytest.fail("Cards are not equal")