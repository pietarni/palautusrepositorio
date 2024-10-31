import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    
    def test_search_works_for_real_player(self):
        self.assertEqual(self.stats.search("Semenko"),self.stats._players[0])

    def test_search_works_for_nonexistant_player(self):
        self.assertEqual(self.stats.search("fdsafasdf"),None)

    def test_team_works(self):
        self.assertEqual(self.stats.team("EDM"),[self.stats._players[0],self.stats._players[2],self.stats._players[4]])

    def test_top_points(self):
        self.assertEqual(self.stats.top(0,SortBy.POINTS),[self.stats._players[4]])

    def test_top_goals(self):
        self.assertEqual(self.stats.top(0,SortBy.GOALS),[self.stats._players[1]])

    def test_top_assists(self):
        self.assertEqual(self.stats.top(0,SortBy.ASSISTS),[self.stats._players[4]])
