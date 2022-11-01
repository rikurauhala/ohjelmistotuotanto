import unittest

from player import Player
from statistics import Statistics


players = [
    Player("Semenko", "EDM", 4, 12),
    Player("Lemieux", "PIT", 45, 54),
    Player("Kurri",   "EDM", 37, 53),
    Player("Yzerman", "DET", 42, 56),
    Player("Gretzky", "EDM", 35, 89)
]

class PlayerReaderStub:
    def get_players(self):
        return players


class TestStatistics(unittest.TestCase):
    def setUp(self):
        reader = PlayerReaderStub()
        self.statistics = Statistics(reader)

    def test_player_search(self):
        for player in players:
            player_object = self.statistics.search(player.name)
            self.assertEqual(player_object.name, player.name)
        player_none = self.statistics.search("Koivu")
        self.assertEqual(player_none, None)

    def test_team_list(self):
        expected_list = [players[0], players[2], players[4]]
        team_name = players[0].team
        actual_list = self.statistics.team(team_name)
        self.assertEqual(expected_list, actual_list)

    def test_top_list(self):
        top_players = self.statistics.top(3)
        self.assertEqual(top_players[0].name, players[4].name)
        self.assertEqual(top_players[1].name, players[1].name)
        self.assertEqual(top_players[2].name, players[3].name)
