from cards_proj.src.cards import Card
import pytest

def test_no_path_raise():
    with pytest.raises(TypeError):
        Card.CardsDB()