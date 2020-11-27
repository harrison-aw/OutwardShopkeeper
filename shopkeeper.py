from typing import List, Set, Any, Union

import cvxpy as cp

from inventory import Inventory
from item import Item
from recipe import Recipe

__all__ = ['Shopkeeper']


class Shopkeeper:
    def __init__(self, inventory: Inventory, items: List[Item],
                 recipes: List[Recipe]) -> None:
        self.inventory = inventory
        self.items = items
        self.recipes = recipes

    def __repr__(self) -> str:
        cls_name = type(self).__name__
        inventory = repr(self.inventory)
        items = repr(self.items)
        recipes = repr(self.recipes)
        return f'{cls_name}({inventory}, {items}, {recipes})'

    def __eq__(self, other: Any) -> Union[bool, type(NotImplemented)]:
        if isinstance(other, Shopkeeper):
            return (self.inventory == other.inventory
                    and self.items == other.items
                    and self.recipes == other.recipes)
        else:
            return NotImplemented

    def possible_recipes(self) -> Set[Recipe]:
        current_items = set(self.inventory.items)
        return {recipe
                for recipe in self.recipes
                if all(ingredient in current_items
                       for ingredient in recipe.ingredients())}

    def possible_items(self) -> Set[str]:
        current_items = set(self.inventory.items)
        possible_recipes = {recipe.name for recipe in self.possible_recipes()}
        return current_items | possible_recipes

    def sell_price(self, item_name: str) -> int:
        return next(item.sell for item in self.items if item.name == item_name)

    def mi_problem(self):
        variables = {item: cp.Variable(name=item, integer=True)
                     for item in self.possible_items()}
        objective = cp.Maximize(sum(shopkeeper.sell_price(item) * variable
                                    for item, variable in variables.items()))

        constraints = [variable >= 0 for variable in variables.values()]
        for item in shopkeeper.inventory.items:
            used_in = {recipe
                       for recipe in shopkeeper.possible_recipes()
                       if item in recipe.ingredients()}
            constraint = sum((recipe.quantity_required(item)
                              / recipe.quantity
                              * variables[recipe.name]
                              for recipe in used_in),
                             variables[item])
            constraints.append(constraint == shopkeeper.inventory.items[item])

        problem = cp.Problem(objective, constraints)
        problem.solve(solver=cp.GLPK_MI)
        return problem

    def items_to_sell(self):
        problem = self.mi_problem()
        problem.solve(solver=cp.GLPK_MI)
        return {variable.name(): int(problem.solution.primal_vars[id_])
                for id_, variable in enumerate(problem.variables())}

    def gross_revenue(self):
        problem = self.mi_problem()
        problem.solve(solver=cp.GLPK_MI)
        return int(problem.solution.opt_val)


if __name__ == '__main__':
    from item import read_items
    from recipe import read_recipes
    from inventory import read_inventory

    shopkeeper = Shopkeeper(read_inventory('data/inventory.csv'),
                            read_items('data/items.csv'),
                            read_recipes('data/recipes.csv'))

    for item, quantity in shopkeeper.items_to_sell().items():
        print(f'{item}: {quantity}')
    print(f'{shopkeeper.gross_revenue()} silver')
