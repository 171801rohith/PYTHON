from cards_proj.src.cards import Card
import pytest

def test_to_dict():
    # Given
    cl = Card("something", "brain", "todo", 123)
    # When
    c2 = cl.to_dict()
    # Then
    c2_expected = {"summary": "something", "owner": "brain", "state": "todo", "id": 123}
    assert c2 == c2_expected