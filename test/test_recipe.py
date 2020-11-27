import pytest

from recipe import Recipe, read_recipes


@pytest.fixture
def recipe():
    return Recipe(3, 'Bullet', 'Iron Scrap', 'Thick Oil', None, None)


def test_quantity(recipe):
    assert recipe.quantity == 3


def test_name(recipe):
    assert recipe.name == 'Bullet'


def test_ingredient1(recipe):
    assert recipe.ingredient1 == 'Iron Scrap'


def test_ingredient2(recipe):
    assert recipe.ingredient2 == 'Thick Oil'


def test_ingredient3(recipe):
    assert recipe.ingredient3 is None


def test_ingredient4(recipe):
    assert recipe.ingredient4 is None


def test_ingredients(recipe):
    assert recipe.ingredients() == {'Iron Scrap', 'Thick Oil'}


def test_quantity_required(recipe):
    assert recipe.quantity_required('Iron Scrap') == 1


def test_quantity_required_is_zero(recipe):
    assert recipe.quantity_required('non ingredient') == 0


@pytest.fixture
def data_file(mocker):
    return mocker.mock_open(read_data='1,Bandages,Linen Cloth,Linen Cloth,,\n'
                                      '1,Bolt Rag,Linen Cloth,Larva Egg,,')


def test_read_recipes(mocker, data_file):
    mocker.patch('builtins.open', data_file)
    assert read_recipes('test.csv') \
           == [Recipe(1, 'Bandages', 'Linen Cloth', 'Linen Cloth', None, None),
               Recipe(1, 'Bolt Rag', 'Linen Cloth', 'Larva Egg', None, None)]
