from player_reader import PlayerReader
from sort_by import SortBy
from statistics import Statistics


def main():
    reader = PlayerReader()
    stats = Statistics(reader)
    top_scorers = stats.top(10)

    print("Top point getters:")
    for player in top_scorers:
        print(player)

    print("Top point getters:")
    for player in stats.top(10, SortBy.POINTS):
        print(player)

    for player in stats.top(10):
        print(player)

    print("Top point goal scorers:")
    for player in stats.top(10, SortBy.GOALS):
        print(player)

    print("Top by assists:")
    for player in stats.top(10, SortBy.ASSISTS):
        print(player)


if __name__ == "__main__":
    main()
