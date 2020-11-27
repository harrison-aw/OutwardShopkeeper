from typing import NamedTuple, Union, List, Set
from csv import reader

__all__ = ['Recipe', 'read_recipes']


class Recipe(NamedTuple):
    quantity: int
    name: str
    ingredient1: str
    ingredient2: Union[str, None] = None
    ingredient3: Union[str, None] = None
    ingredient4: Union[str, None] = None

    def ingredients(self) -> Set[str]:
        ingredients = {self.ingredient1}
        if self.ingredient2:
            ingredients.add(self.ingredient2)
        if self.ingredient3:
            ingredients.add(self.ingredient3)
        if self.ingredient4:
            ingredients.add(self.ingredient4)
        return ingredients

    def quantity_required(self, ingredient_name: str) -> int:
        quantity = 0
        for ingredient in (self.ingredient1,
                           self.ingredient2,
                           self.ingredient3,
                           self.ingredient4):
            if ingredient == ingredient_name:
                quantity += 1
        return quantity


def read_recipes(filename: str) -> List[Recipe]:
    with open(filename) as fp:
        recipes = [Recipe(int(quantity), name,
                          ingredient1,
                          ingredient2 or None,
                          ingredient3 or None,
                          ingredient4 or None)
                   for (quantity, name,
                        ingredient1,
                        ingredient2,
                        ingredient3,
                        ingredient4) in reader(fp)]
    return recipes


if __name__ == '__main__':
    print(read_recipes('data/recipes.csv'))
