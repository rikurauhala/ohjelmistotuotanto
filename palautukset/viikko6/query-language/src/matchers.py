class All:
    def __init__(self):
        pass

    def test(self, player):
        return True


class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False
        return True


class Not:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return True
        return False


class HasAtLeast:
    def __init__(self, matcher, value, attr):
        self._matcher = matcher
        self._value = value
        self._attr = attr

    def test(self, player):
        if not self._matcher.test(player):
            return False
        player_value = getattr(player, self._attr)
        return player_value >= self._value


class HasFewerThan:
    def __init__(self, matcher, value, attr):
        self._matcher = matcher
        self._value = value
        self._attr = attr

    def test(self, player):
        if not self._matcher.test(player):
            return False
        player_value = getattr(player, self._attr)
        return player_value < self._value


class Or:
    def __init__(self, matcher, *matchers):
        self._matcher = matcher
        self._matchers = matchers

    def test(self, player):
        if not self._matcher.test(player):
            return False
        for matcher in self._matchers:
            if matcher.test(player):
                return True
        return False


class PlaysIn:
    def __init__(self, matcher, team):
        self._matcher = matcher
        self._team = team

    def test(self, player):
        if not self._matcher.test(player):
            return False
        return player.team == self._team
