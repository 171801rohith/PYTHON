from cards_proj.src.cards import Card

class TestEquality:
    def test_equalities(self):
        c1 = Card("Something", "Brain", "todo", 123)
        c2 = Card("Something", "Brain", "todo", 123)
        assert c1 == c2


    def test_equalities_with_diff_ids(self):
        c1 = Card("Something", "Brain", "todo", 123)
        c2 = Card("Something", "Brain", "todo", 456)
        assert c1 == c2


    def test_inequality(self):
        cl = Card("something", "brain", "todo", 123)
        c2 = Card("completely different", "okken", "done", 123)
        assert cl != c2