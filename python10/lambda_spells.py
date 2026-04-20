# from typing import Callable, collection

# DELETE THIS
from pprint import pprint

def artifact_sorter(artifacts):
    return sorted(artifacts, key=lambda val: val['power'], reverse=True)

def power_filter(mages, min_power):
    return filter(mages, function=lambda val: val['power'] >= min_power)

if __name__ == "__main__":
    artifacts = [{'name': 'Wind Cloak', 'power': 103, 'type': 'weapon'},
                 {'name': 'Storm Crown', 'power': 99, 'type': 'relic'},
                 {'name': 'Wind Cloak', 'power': 81, 'type': 'weapon'},
                 {'name': 'Crystal Orb', 'power': 72, 'type': 'weapon'}]

    print("Testing artifact sorter...")
    pprint(artifact_sorter(artifacts))
    pprint(power_filter(artifacts))
