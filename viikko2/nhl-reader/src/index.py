from player import Player
from PlayerReader import PlayerReader
from PlayerStats import PlayerStats
from rich.table import Table
from rich.console import Console

def main():
    console = Console()
    while(True):
        season = input("Enter the season URL [2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25/]: ")
        url = "https://studies.cs.helsinki.fi/nhlstats/"+season+"/players"
        reader = PlayerReader(url)
        stats = PlayerStats(reader)

        nationality = input("Enter the nationality: ")
        players = stats.top_scorers_by_nationality(nationality)

        
        table = Table(title="Top Scorers of "+nationality+" for season " + season)

        table.add_column("Name", style="cyan")
        table.add_column("Team", style="magenta")
        table.add_column("Goals", style="green")
        table.add_column("Assists", style="blue")
        table.add_column("Points", style="yellow")

        for player in players:
            table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.points))

        console.print(table)

main()