players: dict[str, dict[str, str | int]] = {
    "alice": {
        "level": 41,
        "total_score": 2824,
        "sessions_played": 13,
        "favorite_mode": "ranked",
        "achievements_count": 5,
    },
    "bob": {
        "level": 16,
        "total_score": 4657,
        "sessions_played": 27,
        "favorite_mode": "ranked",
        "achievements_count": 2,
    },
    "charlie": {
        "level": 44,
        "total_score": 4657,
        "sessions_played": 21,
        "favorite_mode": "ranked",
        "achievements_count": 7,
    },
    "diana": {
        "level": 3,
        "total_score": 2000,
        "sessions_played": 21,
        "favorite_mode": "casual",
        "achievements_count": 4,
    },
    "eve": {
        "level": 33,
        "total_score": 1488,
        "sessions_played": 81,
        "favorite_mode": "casual",
        "achievements_count": 7,
    },
    "frank": {
        "level": 15,
        "total_score": 8359,
        "sessions_played": 85,
        "favorite_mode": "competitive",
        "achievements_count": 1,
    },
}
sessions = [
    {
        "player": "bob",
        "duration_minutes": 94,
        "score": 1831,
        "mode": "competitive",
        "completed": False,
        "achievements": "speed_runner",
    },
    {
        "player": "bob",
        "duration_minutes": 102,
        "score": 1478,
        "mode": "casual",
        "completed": True,
        "achievements": "combo_king",
    },
    {
        "player": "alice",
        "duration_minutes": 50,
        "score": 1508,
        "mode": "ranked",
        "completed": False,
        "achievements": "first_blood",
    },
    {
        "player": "frank",
        "duration_minutes": 63,
        "score": 2296,
        "mode": "casual",
        "completed": False,
        "achievements": "level_master",
    },
    {
        "player": "eve",
        "duration_minutes": 42,
        "score": 2674,
        "mode": "ranked",
        "completed": False,
        "achievements": "treasure_seeker",
    },
    {
        "player": "frank",
        "duration_minutes": 13,
        "score": 287,
        "mode": "ranked",
        "completed": True,
        "achievements": "boss_hunter",
    },
    {
        "player": "alice",
        "duration_minutes": 114,
        "score": 1053,
        "mode": "casual",
        "completed": False,
        "achievements": "boss_hunter",
    },
    {
        "player": "diana",
        "duration_minutes": 86,
        "score": 1594,
        "mode": "casual",
        "completed": False,
        "achievements": "pixel_perfect",
    },
    {
        "player": "bob",
        "duration_minutes": 90,
        "score": 1193,
        "mode": "ranked",
        "completed": True,
        "achievements": "speed_runner",
    },
    {
        "player": "eve",
        "duration_minutes": 98,
        "score": 1102,
        "mode": "casual",
        "completed": False,
        "achievements": "combo_king",
    },
]
game_modes = ["casual", "competitive", "ranked"]
achievements = [
    "first_blood",
    "level_master",
    "speed_runner",
    "treasure_seeker",
    "boss_hunter",
    "pixel_perfect",
    "combo_king",
    "explorer",
]


def main():
    # ================================================
    print("=== Game Analytics Dashboard ===\n")
    # ================================================
    print("=== List Comprehension Examples ===")

    high_scorers = [player
                    for player in players
                    if players[player]["total_score"] > 2000]
    print("High scorers (>2000):", high_scorers)

    scores_doubled = [players[player]["total_score"] * 2
                      for player in players]
    print("Scores doubled:", scores_doubled)

    active_players = [player
                      for player in players
                      if players[player]["sessions_played"] > 25]
    print("Active players:", active_players)
    print()

    # ================================================
    print("=== Dict Comprehension Examples ===")

    player_scores = {player: players[player]["total_score"]
                     for player in players}
    print("Player scores:", player_scores)

    score_categories = {
            'high': len([player for player in players
                         if players[player]["total_score"] > 2000]),

            'medium': len([player for player in players
                          if players[player]["total_score"] <= 2000
                          and players[player]["total_score"] >= 1500]),

            'low': len([player for player in players
                        if players[player]["total_score"] < 1500])
            }
    print("Score categories:", score_categories)

    achievement_counts = {player: players[player]["achievements_count"]
                          for player in players}
    print("Achievement counts:", achievement_counts)
    print()

    # ================================================
    print("=== Set Comprehension Examples ===")

    unique_players = {session["player"] for session in sessions}
    print("Unique players:", unique_players)

    unique_achievements = {session['achievements']
                           for session in sessions}
    print("Unique achievements:", unique_achievements)

    active_game_modes = {
            session["mode"] for session in sessions
            if len([s["mode"] for s in sessions
                    if s["mode"] == session["mode"]]) > len(session)/2
            }
    print("Active regions:", active_game_modes)
    print()

    # ================================================
    print("=== Combined Analysis ===")

    total_players = len({session["player"] for session in sessions})
    print("Total players:", total_players)

    total_unique_achievements = len({session["achievements"]
                                     for session in sessions})
    print("Total unique achievements:", total_unique_achievements)

    score_sum: int = sum([players[player]["total_score"]
                          for player in players])
    players_count: int = len({player for player in players})
    average: float = score_sum / players_count
    print("Average score:", average)

    top_performer = {player: players[player]
                     for player in players
                     if players[player]['total_score'] ==
                     max([players[player]["total_score"]
                          for player in players])}
    name = [*top_performer][0]
    print(F"Top performer: {name} " +
          F"({top_performer[name]['total_score']} points," +
          F" {top_performer[name]['achievements_count']} achievements)")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Unexpected error:", e)
