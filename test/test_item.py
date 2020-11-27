import pytest

from item import Item, read_items


@pytest.fixture
def item():
    return Item('Test Item', 3, 1)


def test_name(item):
    assert item.name == 'Test Item'


def test_buy(item):
    assert item.buy == 3


def test_sell(item):
    assert item.sell == 1


@pytest.fixture
def data_file(mocker):
    return mocker.mock_open(read_data='Bandages,3,1\nBolt Rag,15,4')


def test_read_items(mocker, data_file):
    mocker.patch('builtins.open', data_file)
    assert read_items('test.sv') == [Item('Bandages', 3, 1),
                                     Item('Bolt Rag', 15, 4)]


