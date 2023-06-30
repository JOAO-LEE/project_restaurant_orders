from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    """Test if two ingredients of the same type are equal"""
    ingredient_one = Ingredient("presunto")
    ingredient_two = Ingredient("presunto")
    assert ingredient_one.__eq__(ingredient_two) is True

    """Test if two different ingredients are not equal"""
    ingredient_one = Ingredient("presunto")
    ingredient_two = Ingredient("ovo")
    assert ingredient_one.__eq__(ingredient_two) is False

    """"Test if an invalid ingredient has no restrictions"""
    ingredient_x = Ingredient("x")
    assert ingredient_x.restrictions == set()
    assert ingredient_x.name == "x"

    """Test successful ingredient name insertion"""
    ingredient_shrimp = Ingredient("camarão")
    assert ingredient_shrimp.__repr__() == "Ingredient('camarão')"

    """Test if ingredients of the same type have the same hash"""
    ingredient_other_shrimp = Ingredient("camarão")
    assert ingredient_shrimp.__hash__() == ingredient_other_shrimp.__hash__()

    """Test if different ingredients does not have the same hash"""
    ingredient_egg = Ingredient("egg")
    assert ingredient_egg.__hash__() != ingredient_shrimp.__hash__()
