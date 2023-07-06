import csv

from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.data = source_path
        self.new_dish = dict()
        self.dishes = self.create_dishes(self.data)

    def create_dishes(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                rows = csv.DictReader(file, delimiter=",")
                dishes = list(rows)

                for food in dishes:
                    if food["dish"] not in self.new_dish:
                        dish = Dish(food["dish"], float(food["price"]))
                        self.new_dish[food["dish"]] = dish
                    self.new_dish[food["dish"]].add_ingredient_dependency(
                        Ingredient(food["ingredient"]),
                        int(food["recipe_amount"]),
                    )
                return set(self.new_dish.values())
        except FileNotFoundError:
            raise FileNotFoundError()


# new_menu = MenuData("data/menu_base_data.csv")
# print(new_menu.dishes)
