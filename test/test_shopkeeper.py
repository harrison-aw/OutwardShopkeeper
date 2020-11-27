import pytest

from inventory import Inventory
from item import Item
from recipe import Recipe
from shopkeeper import Shopkeeper


@pytest.fixture
def inventory():
    return Inventory((5, 'Linen Cloth'), (4, 'Thick Oil'), (6, 'Iron Scrap'))


@pytest.fixture
def items():
    return [Item(name='Bandages', buy=3, sell=1),
            Item(name='Bolt Rag', buy=15, sell=4),
            Item(name='Bullet', buy=3, sell=1),
            Item(name='Fire Rag', buy=15, sell=4),
            Item(name='Grilled Crabeye Seed', buy=3, sell=1),
            Item(name='Ice Rag', buy=15, sell=4),
            Item(name='Iron Scrap', buy=3, sell=1),
            Item(name='Larva Egg', buy=15, sell=4),
            Item(name='Linen Cloth', buy=1, sell=0),
            Item(name='Poison Rag', buy=15, sell=4),
            Item(name='Seaweed', buy=3, sell=1),
            Item(name='Thick Oil', buy=2, sell=1)]


@pytest.fixture
def recipes():
    return [Recipe(quantity=1, name='Bandages',
                   ingredient1='Linen Cloth', ingredient2='Linen Cloth'),
            Recipe(quantity=1, name='Bolt Rag',
                   ingredient1='Linen Cloth', ingredient2='Larva Egg'),
            Recipe(quantity=3, name='Bullet',
                   ingredient1='Iron Scrap', ingredient2='Thick Oil'),
            Recipe(quantity=1, name='Fire Rag',
                   ingredient1='Linen Cloth', ingredient2='Thick Oil'),
            Recipe(quantity=1, name='Ice Rag',
                   ingredient1='Linen Cloth', ingredient2='Seaweed'),
            Recipe(quantity=1, name='Poison Rag',
                   ingredient1='Linen Cloth', ingredient2='Grilled Crabeye Seed')]


@pytest.fixture
def shopkeeper(inventory, items, recipes):
    return Shopkeeper(inventory, items, recipes)


def test_inventory(shopkeeper, inventory):
    assert shopkeeper.inventory == inventory


def test_items(shopkeeper, items):
    assert shopkeeper.items == items


def test_recipes(shopkeeper, recipes):
    assert shopkeeper.recipes == recipes


def test_possible_recipes(shopkeeper):
    assert shopkeeper.possible_recipes() \
           == {Recipe(quantity=1, name='Bandages',
                      ingredient1='Linen Cloth', ingredient2='Linen Cloth'),
               Recipe(quantity=1, name='Fire Rag',
                      ingredient1='Linen Cloth', ingredient2='Thick Oil'),
               Recipe(quantity=3, name='Bullet',
                      ingredient1='Iron Scrap', ingredient2='Thick Oil')}


def test_possible_items(shopkeeper):
    assert shopkeeper.possible_items() \
           == {'Linen Cloth', 'Bandages', 'Iron Scrap', 'Fire Rag',
               'Thick Oil', 'Bullet'}


def test_sell_price(shopkeeper):
    assert shopkeeper.sell_price('Iron Scrap') == 1