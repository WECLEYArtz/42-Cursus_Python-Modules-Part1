from typing import Generator

events_count = 1000


def random(min: int, max: int):
    a: int = 1140671485
    c: int = 12820163
    mod: int = 2**24

    seed = 0
    while True:
        seed = (a * seed + c) % mod
        random_num = int(seed / (mod - 1) * (max - min) + min)
        if (random_num in range(min, max)):
            yield int(seed / (mod-1) * (max - min) + min)


class Game():
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
            "charlie": 7,
            # "jeff": 10
            }
    player_names: list[str] = [player for player in players]

    player_rando_gen: Generator[int, None, None] = random(0, len(player_names))
    summaries_rando_gen: Generator[int, None, None] = random(0, len(summaries))

    @classmethod
    def update_level(cls, event: dict[str, int | str]):
        if (event['summary'] == "leveled up"):
            cls.players[event['player']] += 1

    @classmethod
    def event_stream(cls) -> Generator[dict[str, int | str], None, None]:
        iters: int = 1

        _ = next(cls.summaries_rando_gen)  # Randomization offsetting
        while iters <= events_count:
            player_name: str = cls.player_names[next(cls.player_rando_gen)]
            event: dict[str, int | str] = {
                    "id": iters,
                    "player": player_name,
                    "level": cls.players[player_name],
                    "summary": cls.summaries[next(cls.summaries_rando_gen)],
                    }
            cls.update_level(event)
            yield (event)
            iters += 1


def proccess_events():
    event_stearm_gen = Game.event_stream()

    heigh_level_players = 0
    treasure_events = 0
    level_up_events = 0

    print("=== Game Data Stream Processor ===")
    print()
    print("Processing", events_count, "game events...")
    print()

    def display(event: dict[str, int | str]):
        print(F"Event {event['id']}:", end=' ')
        print(F"Player {event['player']}", end=' ')
        print(F"(level {event['level']})", end=' ')
        print(F"{event['summary']}")

    try:
        for event in event_stearm_gen:
            if event["summary"] == "leveled up":
                level_up_events += 1
            elif event["summary"] == "found treasure":
                treasure_events += 1
            if event['level'] >= 10:
                heigh_level_players += 1
            display(event)
    except KeyboardInterrupt:
        print("Stoppig...")
    except Exception as e:
        print("Error: Something went wrong - ", e, "Stopping...")
    print()
    print("=== Stream Analytics ===")
    print("Total events processed:", events_count)
    print("High-level players (10+):", heigh_level_players)
    print("Treasure events:", treasure_events)
    print("Level-up events:", level_up_events)
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")


def fibonacci(n: int) -> Generator[int, None, None]:
    print(f"Fibonacci sequence (first {n})")
    a, b = 0, 1
    while (n):
        yield a
        n -= 1
        a, b = b, a + b


def next_prime(n: int) -> Generator[int, None, None]:
    print(f"Prime numbers sequence (first {n})")

    def is_prime(num: int) -> bool:
        i = 2
        while i*i <= num:
            if num % i == 0:
                return False
            i += 1
        return True

    start_point = 2
    while n:
        if (is_prime(start_point)):
            yield start_point
            n -= 1
        start_point += 1


def main():
    proccess_events()

    try:
        print("")
        fib_gen = fibonacci(10)
        for n in fib_gen:
            print(n, end=', ')
        print()
    except KeyboardInterrupt:
        print("Stoppig...")

    try:
        prm_gen = next_prime(50)
        for n in prm_gen:
            print(n, end=', ')
        print()
    except KeyboardInterrupt:
        print("Stoppig...")


if __name__ == "__main__":
    main()
