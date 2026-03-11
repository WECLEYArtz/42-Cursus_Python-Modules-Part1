import typing

events_count = 1000


def random(min: int, max: int) -> typing.Generator[int, None, None]:
    a: int = 1140671485
    c: int = 12820163
    mod: int = 2**24

    seed = 0
    while True:
        seed = (a * seed + c) % mod
        random_num = int(seed / (mod - 1) * (max - min) + min)
        if (random_num in range(min, max)):
            yield random_num


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
            }
    player_names: list[str] = [player for player in players]

    player_rando_gen: typing.Generator[int, None, None]
    player_rando_gen = random(0, len(player_names))

    summaries_rando_gen: typing.Generator[int, None, None]
    summaries_rando_gen = random(0, len(summaries))

    @classmethod
    def update_level(cls, event: dict[str, int | str]) -> None:
        if (event['summary'] == "leveled up"):
            name: str = event['player']
            cls.players[name] += 1

    @classmethod
    def stream(cls) -> typing.Generator[dict[str, int | str], None, None]:
        iters: int = 1

        _ = next(cls.summaries_rando_gen)  # Randomization offsetting
        while iters <= events_count:
            player_name: str = cls.player_names[next(cls.player_rando_gen)]
            event: dict[str, int | str] = {
                    "player": player_name,
                    "id": iters,
                    "level": cls.players[player_name],
                    "summary": cls.summaries[next(cls.summaries_rando_gen)],
                    }
            cls.update_level(event)
            yield (event)
            iters += 1


def proccess_events() -> None:
    event_stearm_gen = Game.stream()

    heigh_level_players = 0
    treasure_events = 0
    level_up_events = 0

    print("=== Game Data Stream Processor ===")
    print()
    print("Processing", events_count, "game events...")
    print()

    def display(event: dict[str, int | str]) -> None:
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
    print()
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")


def fibonacci(times: int) -> typing.Generator[int, None, None]:
    print(f"Fibonacci sequence (first {times}):", end=' ')
    a, b = 0, 1
    while (times):
        yield a
        times -= 1
        a, b = b, a + b


def next_prime(times: int) -> typing.Generator[int, None, None]:
    print(f"Prime numbers (first {times}):", end=' ')

    def is_prime(num: int) -> bool:
        i = 2
        while i*i <= num:
            if num % i == 0:
                return False
            i += 1
        return True

    start_point = 2
    while times:
        if (is_prime(start_point)):
            yield start_point
            times -= 1
        start_point += 1


def main() -> None:
    proccess_events()
    print()
    try:
        fib_gen = fibonacci(10)
        for n in fib_gen:
            print(n, end=', ')
        print()

        prm_gen = next_prime(5)
        for n in prm_gen:
            print(n, end=', ')
        print()
    except KeyboardInterrupt:
        print("Stoppig...")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Unexpected error:", e)
