from matchers import All, And, HasAtLeast, HasFewerThan, PlaysIn


class QueryBuilder:
    def __init__(self, matcher=And()):
        self.matcher = matcher

    def build(self):
        return self.matcher

    def all(self):
        return QueryBuilder(
            All(self.matcher)
        )

    def has_at_least(self, value, attr):
        return QueryBuilder(
            HasAtLeast(
                self.matcher,
                value,
                attr
            )
        )

    def has_fewer_than(self, value, attr):
        return QueryBuilder(
            HasFewerThan(
                self.matcher,
                value,
                attr
            )
        )

    def plays_in(self, team):
        return QueryBuilder(
            PlaysIn(
                self.matcher,
                team
            )
        )
