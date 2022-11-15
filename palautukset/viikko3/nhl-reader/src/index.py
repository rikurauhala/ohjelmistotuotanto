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

    print("NHL players from Finland:")
    for player in players:
        if player.nationality == "FIN":
            print(player)


if __name__ == "__main__":
    main()
