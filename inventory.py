from typing import Any, Union
from csv import reader


class Inventory:
    def __init__(self, *items: (int, str)) -> None:
        self.items = {item: quantity for quantity, item in items}

    def __repr__(self) -> str:
        cls_name = type(self).__name__
        args = tuple((quantity, item) for item, quantity in self.items.items())
        return f'{cls_name}{args}'

    def __eq__(self, other: Any) -> Union[bool, type(NotImplemented)]:
        if isinstance(other, Inventory):
            return self.items == other.items
        else:
            return NotImplemented


def read_inventory(filename: str) -> Inventory:
    with open(filename) as fp:
        items = [(int(quantity), item) for quantity, item in reader(fp)]
    return Inventory(*items)


if __name__ == '__main__':
    print(read_inventory('data/inventory.csv'))
