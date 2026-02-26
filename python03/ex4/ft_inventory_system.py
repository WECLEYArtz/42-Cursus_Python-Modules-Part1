import sys


class Inventory():
    def __init__(self, argv: list[str]):
        self.items: dict[str, int] = self.parse_argument(argv)
        self.items_count: int = self.update_items_count()

    @staticmethod
    def percentage(val: int, total: int) -> float:
        return ((val / total) * 100)

    @staticmethod
    def parse_argument(argv: list[str]) -> dict[str, int]:
        items: dict[str, int] = {}

        for arg in argv:
            if (not arg):
                raise ValueError("Error: No value was given")

            sep_index: int = 0
            for char in arg:
                if char == ':':
                    break
                sep_index += 1

            if (sep_index == 0):
                raise ValueError("Error: No first value was given")
            elif (sep_index == len(arg)):
                raise ValueError("Error: No second value was given")

            # print("parsing:", arg, "into:",
            #       arg[0:sep_index], int(arg[sep_index+1:]))
            items.update({arg[0:sep_index]: int(arg[sep_index+1:])})
        return items

    def show_analysis(self):
        print("=== Inventory System Analysis ===")
        print("Total items in inventory:", self.items_count)
        print("Unique item types:", self.get_unique_count())

    def show_current_info(self):
        print("=== Current Inventory ===")
        for k, v in self.items.items():
            print(F"{k}: {v} units", end='')
            print(F"({self.percentage(v, self.items_count):.1f}%)")

    def show_statistics(self):
        most: str = max(self.items, key=self.items.get)
        least: str = min(self.items, key=self.items.get)
        print("=== Inventory Statistics ===")

        print(F"Most abundant: {most}", end='')
        print(F" ({self.items.get(most)}",
              "unit)" if self.items.get(most) == 1 else "units)")

        print(F"Least abundant: {least}", end='')
        print(F" ({self.items.get(least)}",
              "unit)" if self.items.get(least) == 1 else "units)")

    def show_categories(self):
        print("=== Item Categories ===")
        moderate: dict[str, int] = {}
        scarce: dict[str, int] = {}
        for key, value in self.items.items():
            if self.percentage(value, self.items_count) >= 40:
                moderate.update({key: value})
            else:
                scarce.update({key: value})
        print("Moderate:", moderate)
        print("Scarce:", scarce)

    def show_suggestion(self):
        low_stock: str = " "
        print("=== Management Suggestions ===")
        print("Restock needed:", end='')

        for key, value in self.items.items():
            if self.percentage(value, self.items_count) <= 10:
                low_stock += key+", "
        print(low_stock[:-2])

    def show_properties_demo(self):
        keys: str = ""
        values: str = ""

        print("=== Dictionary Properties Demo ===")

        print("Dictionary keys: ", end='')
        for key in self.items.keys():
            keys += key+', '
        print(keys[:-2])

        print("Dictionary values: ", end='')
        for value in self.items.values():
            values += str(value)+', '
        print(values[:-2])

        item_lookup = "sword"
        print("Sample lookup - ", end='')
        print(item_lookup, "in inventory:",  item_lookup in self.items)

    def get_unique_count(self) -> int:
        item_names = [item for item in self.items]
        return (len({*item_names}))

    def update_items_count(self):
        count = 0
        for _, v in self.items.items():
            count += v
        return count


if __name__ == "__main__":
    try:
        inv1 = Inventory(sys.argv[1:])
        print()
        inv1.show_analysis()
        print()
        inv1.show_current_info()
        print()
        inv1.show_statistics()
        print()
        inv1.show_categories()
        print()
        inv1.show_suggestion()
        print()
        inv1.show_properties_demo()
    except ValueError as e:
        print(e)
    except Exception as e:
        print("Error, something went wrong:")
        print(e)
