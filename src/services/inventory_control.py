from csv import DictReader
from typing import Dict

from src.models.dish import Recipe, Dish
from src.models.ingredient import Ingredient

BASE_INVENTORY = "data/inventory_base_data.csv"

Inventory = Dict[Ingredient, int]


def read_csv_inventory(inventory_file_path=BASE_INVENTORY) -> Inventory:
    inventory = dict()

    with open(inventory_file_path, encoding="utf-8") as file:
        for row in DictReader(file):
            ingredient = Ingredient(row["ingredient"])
            inventory[ingredient] = int(row["initial_amount"])

    return inventory


# Req 5
class InventoryMapping:
    def __init__(self, inventory_file_path=BASE_INVENTORY) -> None:
        self.inventory = read_csv_inventory(inventory_file_path)

    # Req 5.1
    def check_recipe_availability(self, recipe: Recipe) -> bool:
        for ingredient in recipe.get_ingredients():
            if ingredient not in self.inventory.keys():
                return False
            else:
                return True

    # Req 5.2
    def consume_recipe(self, recipe: Recipe) -> None:
        pass


# new_inventory = InventoryMapping()
# new_dish = Dish("lasanha de presunto", 25.90)
# new_dish.add_ingredient_dependency(Ingredient("queijo mussarela"), 15)
# new_dish.add_ingredient_dependency(Ingredient("tomate"), 10)
# new_dish.add_ingredient_dependency(Ingredient("farinha de trigo"), 10)
# new_dish.add_ingredient_dependency(Ingredient("sal"), 5)
# new_dish.add_ingredient_dependency(Ingredient("água"), 10)
# new_dish.add_ingredient_dependency(Ingredient("presunto"), 15)
# # print(new_dish.get_ingredients())
# print(new_inventory.check_recipe_availability(new_dish))
