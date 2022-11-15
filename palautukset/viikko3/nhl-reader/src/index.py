import requests

from player import Player


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()

    players = []
    for player_dict in response:
        player = Player(
            player_dict["name"],
            player_dict["team"],
            player_dict["nationality"],
            player_dict["goals"],
            player_dict["assists"]
        )
        players.append(player)

    filtered_players = sorted(
        players,
        key=lambda player: player.score,
        reverse=True
    )

    print("NHL players from Finland")
    print("")
    print("NAME                 TEAM  SCORE")
    for player in filtered_players:
        if player.nationality == "FIN":
            print(player)


if __name__ == "__main__":
    main()
