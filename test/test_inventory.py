import pytest

from inventory import Inventory, read_inventory


@pytest.fixture
def inventory():
    return Inventory((5, 'Linen Cloth'), (4, 'Thick Oil'), (6, 'Iron Scrap'))


def test_items(inventory):
    assert inventory.items == {'Linen Cloth': 5, 'Thick Oil': 4, 'Iron Scrap': 6}


def test_repr(inventory):
    assert repr(inventory) \
           == "Inventory((5, 'Linen Cloth'), (4, 'Thick Oil'), (6, 'Iron Scrap'))"


@pytest.fixture
def data_file(mocker):
    return mocker.mock_open(read_data='5,Linen Cloth\n4,Thick Oil\n6,Iron Scrap')


def test_read_inventory(mocker, data_file, inventory):
    mocker.patch('builtins.open', data_file)
    assert read_inventory('test.csv') == inventory
