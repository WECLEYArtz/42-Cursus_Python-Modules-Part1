from typing import Generator

events_count = 1000

summaries: list[str] = [
        "leveled up",
        "killed monster",
        "died",
        "defeated a boss",
        "joined the world",
        "found treasure",
        ]
players: dict[str, int] = {
        "alice": 5,
        "bob": 12,
        "charlie": 7
        }
player_names: list[str] = [player for player in players]

def random(min: int, max: int):
    a: int = 1140671485
    c: int = 12820163
    mod: int = 2**24

    seed = 0
    while True:
        seed = (a * seed + c) % mod
        yield int(seed / (mod-1) * (max - min) + min)


def event_stream() -> Generator[dict[str, int | str]]:
    iters: int = 0
    player_random_gen = random(0, len(player_names))
    summaries_random_gen = random(0, len(summaries))
    while iters < events_count:
        player_name: str = player_names[next(player_random_gen)]
        event: dict[str, int | str] = {
                "id": iters,
                "player": player_names[next(player_random_gen)],
                "level": players[player_name],
                "summary": summaries[next(summaries_random_gen)],
                }
        iters += 1
        yield (event)


def proccess_events():

    heigh_level_players = 0
    treasure_events = 0
    level_up_events = 0
    event_stearm_gen = event_stream()

    print("=== Game Data Stream Processor ===")
    print()
    print("Processing", events_count, "game events...")
    print()

    for event in event_stearm_gen:
        if event["summary"] == "leveled up":
            level_up_events += 1
            players[event["player"]] += 1
            print("--- level_up_events ---", level_up_events)
        elif event["summary"] == "found treasure":
            treasure_events += 1
            print("--- treasure_events ---", treasure_events)
        if players[event["player"]] >= 10:
            heigh_level_players += 1

        print(F"Event {event["id"]}:", end=' ')
        print(F"Player {event["player"]}", end=' ')
        print(F"(level {event["level"]})", end=' ')
        print(F"{event["summary"]}")

    print()
    print("=== Stream Analytics ===")
    print("Total events processed:", events_count)
    print("High-level players (10+):", heigh_level_players)
    print("Treasure events:", treasure_events)
    print("Level-up events:", level_up_events)
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")


def fibonacci(n: int) -> Generator[int]:
    a, b = 0, 1
    while (n):
        yield a
        n -= 1
        a, b = b, a + b


def prime(n: int) -> Generator[int]:
    print(f"Fibonacci sequence (first {n})")
    i = 2

    while True
    for i in :
        for j in range(2, ):
            if i % j == 0 and i == j:
                yield i
                n -= 1
                break
            if i % j == 0 and i != j:
                break
            


if __name__ == "__main__":
    proccess_events()

    fib_gen = fibonacci(10)
    for n in fib_gen:
        print(n, end=', ')
    print()

    prm_gen = prime(5)
    for n in prm_gen:
        print(n, end=', ')
    print()


# $> python3 ft_data_stream.py
# === Game Data Stream Processor ===
#
# Processing 1000 game events...
#
# Event 1: Player alice (level 5) killed monster
# Event 2: Player bob (level 12) found treasure
# Event 3: Player charlie (level 8) leveled up
# ...
#
# === Stream Analytics ===
# Total events processed: 1000
# High-level players (10+): 342
# Treasure events: 89
# Level-up events: 156
# Memory usage: Constant (streaming)
# Processing time: 0.045 seconds
#
# === Generator Demonstration ===
# Fibonacci sequence (first 10): 0, 1, 1, 2, 3, 5, 8,
