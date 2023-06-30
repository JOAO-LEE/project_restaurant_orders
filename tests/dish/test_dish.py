from src.models.dish import Dish  # noqa: F401, E261, E501
import pytest
from src.models.ingredient import Restriction, Ingredient


# Req 2
def test_dish():
    """Test successful dish name and pricing"""
    new_dish = Dish("Ravioli Especial de Queijo", 60.99)
    assert new_dish.name == "Ravioli Especial de Queijo"
    assert new_dish.price == 60.99
    assert new_dish.__repr__() == "Dish('Ravioli Especial de Queijo', R$60.99)"
    other_dish = Dish("Ravioli Especial de Queijo", 60.99)

    """Test valid ingredient insertion"""
    ravioli_ingredients = [
        "massa de ravioli",
        "manteiga",
        "creme de leite",
        "queijo mussarela",
        "queijo gorgonzola",
        "queijo parmesão",
        "queijo provolone",
    ]

    for ingredients in ravioli_ingredients:
        new_dish.add_ingredient_dependency(ingredients, 1)
        other_dish.add_ingredient_dependency(ingredients, 1)

    assert new_dish.get_ingredients() == {
        "massa de ravioli",
        "queijo mussarela",
        "creme de leite",
        "queijo parmesão",
        "manteiga",
        "queijo gorgonzola",
        "queijo provolone",
    }

    """Test if two dishes of the same food are the same"""
    assert new_dish.__eq__(other_dish) is True

    """Test if two dishes of the same food have the same hash"""
    assert new_dish.__hash__() == other_dish.__hash__()

    """Test if two dishes of different food does not have the same hash"""
    another_dish = Dish("Lasanha Bolonhesa Especial", 70.99)
    lasagna_ingredients = [
        "massa de lasanha",
        "carne",
        "queijo mussarela",
        "presunto",
        "queijo parmesão",
    ]

    for ingredients in lasagna_ingredients:
        another_dish.add_ingredient_dependency(ingredients, 1)

    assert other_dish.__eq__(another_dish) is False
    assert other_dish.__hash__() != another_dish.__hash__()

    """Test if an error is raised when price is invalid"""
    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        one_more_dish = Dish("Camarão na manteiga", 0)
    """Test restrictions"""
    one_more_dish = Dish("Camarão na manteiga", 54.95)
    one_more_dish.add_ingredient_dependency(Ingredient("camarão"), 1)
    one_more_dish.add_ingredient_dependency(Ingredient("manteiga"), 1)

    assert one_more_dish.get_restrictions() == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
        Restriction.SEAFOOD,
        Restriction.ANIMAL_DERIVED,
        Restriction.LACTOSE,
    }
