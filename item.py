from typing import NamedTuple, List
from csv import reader


__all__ = ['Item', 'read_items']


class Item(NamedTuple):
    name: str
    buy: int
    sell: int


def read_items(filename: str) -> List[Item]:
    with open(filename) as fp:
        items = [Item(name, int(buy), int(sell))
                 for name, buy, sell in reader(fp)]
    return items


if __name__ == '__main__':
    print(read_items('data/items.csv'))
