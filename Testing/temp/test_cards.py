from cards_proj.src.cards import Card


def test_field_access():
    c = Card("Something", "Brain", "todo", 123)
    assert c.summary == "Something"
    assert c.owner == "Brain"
    assert c.state == "todo"
    assert c.id == 123


def test_default():
    c = Card()
    assert c.summary == None
    assert c.owner == None
    assert c.state == "todo"
    assert c.id == None


def test_equalities():
    c1 = Card("Something", "Brain", "todo", 123)
    c2 = Card("Something", "Brain", "todo", 123)
    assert c1 == c2


def test_equalities_with_diff_ids():
    c1 = Card("Something", "Brain", "todo", 123)
    c2 = Card("Something", "Brain", "todo", 456)
    assert c1 == c2


def test_inequality():
    cl = Card("something", "brain", "todo", 123)
    c2 = Card("completely different", "okken", "done", 123)
    assert cl != c2


def test_from_dict():
    cl = Card("something", "brain", "todo", 123)
    c2_dict = {"summary": "something", "owner": "brain", "state": "todo", "id": 123}
    c2 = Card.from_dict(c2_dict)
    assert cl == c2


def test_to_dict():
    cl = Card("something", "brain", "todo", 123)
    c2 = cl.to_dict()
    c2_expected = {"summary": "something", "owner": "brain", "state": "todo", "id": 123}
    assert c2 == c2_expected