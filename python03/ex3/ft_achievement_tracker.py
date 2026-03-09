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
    unique_achv: set[str] = set.union(*achv_sets_list)
    print("All unique achievements:", unique_achv)
    print("Total unique achievements:", len(unique_achv), '\n')

    common_achv: set[str] = set.intersection(*achv_sets_list)
    print("Common to all players: ", common_achv, '\n')

    rare_achv: set[str] = set()
    for _ in achv_sets_list:
        rare_achv |= achv_sets_list[0] - set.union(*achv_sets_list[1:])
        achv_sets_list = achv_sets_list[-1:] + achv_sets_list[:-1]
    print("Rare achievements (1 player):", rare_achv, "\n")

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
        print("Unexcpecetd error", e)
