from player import Player
from PlayerReader import PlayerReader
class PlayerStats:
    def __init__(self, playerReader):    
        self.playerReader = playerReader

    
    def top_scorers_by_nationality(self, country):
        players = self.playerReader.get_players()
        filtered_players = [player for player in players if player.nationality == country]
        return sorted(filtered_players, key=lambda x: x.points, reverse=True)