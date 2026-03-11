import sys


class InventoryError(Exception):
    pass


class Inventory():
    def __init__(self, argv: list[str]):
        self.items: dict[str, int] = self.parse_argument(argv)
        self.items_count: int = self.update_items_count()
        self.items_category: dict[str, dict[str, int]] = {
                "Scarce": {},
                "Moderate": {},
                "Abundant": {},
                }

    @staticmethod
    def percentage(val: int, total: int) -> float:
        return ((val / total) * 100)

    @staticmethod
    def parse_argument(argv: list[str]) -> dict[str, int]:
        argv = [arg for arg in argv if argv]
        if not len(argv):
            raise InventoryError("No scores provided\nUsage: " +
                                 "python3 ft_inventory_system.py " +
                                 "<item1:count> <item2:count> ...")
        items: dict[str, int] = {}

        for arg in argv:
            sep_index: int = 0
            for char in arg:
                if char == ':':
                    break
                sep_index += 1

            if (sep_index == 0):
                raise InventoryError("No first value given (empty:...)")
            elif (sep_index == len(arg) - 1):
                raise InventoryError("No second value given (...:empty)")

            key = arg[0:sep_index]
            val = int(arg[sep_index+1:])
            if val < 0:
                raise InventoryError("Niggative values are not allowed")
            if key in items:
                items[key] += val
            else:
                items.update({key: val})
        return items

    def show_analysis(self) -> None:
        print("=== Inventory System Analysis ===")
        print("Total items in inventory:", self.items_count)
        print("Unique item types:", self.get_unique_count())

    def show_current_info(self) -> None:
        print("=== Current Inventory ===")
        for k, v in self.items.items():
            print(F"{k}: {v} units", end=' ')
            if (not v):
                print("0.0%")
            else:
                print(F"({self.percentage(v, self.items_count):.1f}%)")

    def show_statistics(self) -> None:
        most: str = max(self.items, key=self.items.get)
        least: str = min(self.items, key=self.items.get)
        print("=== Inventory Statistics ===")

        print(F"Most abundant: {most} ({self.items.get(most)}", end=' ')
        print("unit)" if self.items.get(most) == 1 else "units)")

        print(F"least abundant: {least} ({self.items.get(least)}", end=' ')
        print("unit)" if self.items.get(least) == 1 else "units)")

    def show_categories(self) -> None:
        print("=== Item Categories ===")
        for key, value in self.items.items():
            if (not value):
                continue
            percentage = self.percentage(value, self.items_count)
            if percentage > 66.66:
                self.items_category["Abundant"].update({key: value})
            elif percentage > 33.33:
                self.items_category["Moderate"].update({key: value})
            else:
                self.items_category["Scarce"].update({key: value})

        for categ_name in self.items_category.keys():
            print(categ_name+":", self.items_category[categ_name])

    def show_suggestion(self) -> None:
        low_stock: str = " "
        print("=== Management Suggestions ===")
        print("Restock needed:", end='')

        low_stock_list = [key for key, value in self.items.items()
                          if value == min([v for v in self.items.values()])]
        for item in low_stock_list:
            low_stock += item+', '
        print(low_stock[:-2])

    def show_properties_demo(self) -> None:
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

    def update_items_count(self) -> int:
        count = 0
        for _, v in self.items.items():
            count += v
        return count


def main() -> None:
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
    except InventoryError as e:
        print("Error - Couldn't proccess inventory:", e)
    except Exception as e:
        print("Error - something went wrong:", e)


if __name__ == "__main__":
    main()
