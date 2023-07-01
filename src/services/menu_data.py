import csv

from src.models.ingredient import Ingredient
from src.models.dish import Dish


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.data = source_path
        self.created_dishes = set()
        self.dishes = self.create_dishes(self.data)

    def create_dishes(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                _, *file_lines = csv.reader(file, delimiter=",")

                for index in range(0, len(file_lines)):
                    for dish_name, price, ingredient, quantity in file_lines:
                        new_dish = Dish(dish_name, float(price))
                        new_dish.add_ingredient_dependency(
                            Ingredient(ingredient), int(quantity)
                        )
                        # new_dish.recipe
                        self.created_dishes.add(new_dish)
                return self.created_dishes
        except:
            FileNotFoundError()


new_menu = MenuData("data/menu_base_data.csv")
print(new_menu.dishes)
