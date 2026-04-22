def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda val: val['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda val: int(val['power']) >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    powers: list[int] = list(map(lambda m: int(m['power']), mages))
    return ({
        'max_power': max(powers),
        'min_power': min(powers),
        'avg_power': round(sum(powers) / len(powers), 2)
        })


def main() -> None:
    data: list[dict[str, str | int]] = [
            {'name': 'Fire Staff', 'power': 92, 'type': 'relic'},
            {'name': 'Crystal Orb', 'power': 85, 'type': 'weapon'},
            {'name': 'Bazooka', 'power': 4, 'type': 'gun'}]

    print("Testing artifact sorter...")
    sorted_data = artifact_sorter(data)
    print(f"{sorted_data[0]['name']} ({sorted_data[0]['power']} power)",
          "comes before",
          f"{sorted_data[1]['name']} ({sorted_data[1]['power']} power)")
    print()

    print("Testing spell transformer...")
    data = ["fireball", "heal", "shield"]
    transfered_data = spell_transformer(data)
    print(" ".join(transfered_data))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)

# Testing artifact sorter...
# Fire Staff (92 power) comes before Crystal Orb (85 power)
# Testing spell transformer...
# * fireball * * heal * * shield *
