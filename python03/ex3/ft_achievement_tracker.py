def main() -> None:
    players: dict[str, set[str]] = {
        "alice": {
                'first_kill',
                'level_10',
                'treasure_hunter',
                'speed_demon'},
        "bob": {
                'first_kill',
                'level_10',
                'boss_slayer',
                'collector'},
        "charlie": {
                'level_10',
                'treasure_hunter',
                'boss_slayer',
                'speed_demon',
                'perfectionist'}
    }
    achv_sets_list = [players[name] for name in players]

    print("=== Achievement Tracker System ===\n")
    for player in players:
        print(F"Player {player} achievements:", players[player])
    print()

    print("=== Achievement Analytics ===")
    unique: set[str] = set.union(*achv_sets_list)
    print("All unique achievements:", unique)
    print("Total unique achievements:", len(unique), '\n')

    common: set[str] = set.intersection(*achv_sets_list)
    print("Common to all players: ", common, '\n')

    rare: list[str] = []
    rare += players['alice'].difference(players['bob'], players['charlie'])
    rare += players['bob'].difference(players['alice'], players['charlie'])
    rare += players['charlie'].difference(players['alice'], players['bob'])
    print("Rare achievements (1 player):", rare, "\n")

    print("Alice vs Bob common:",
          players["alice"].intersection(players["bob"]))

    print("Alice unique:",
          players["alice"] - players["alice"].intersection(players["bob"]))

    print("Bob unique:",
          players["bob"] - players["alice"].intersection(players["bob"]))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(F"Unexcpecetd error - {e.__class__.__name__}:", e)
