from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    # def test_check_same_ingredient():
    ingredient_one = Ingredient("presunto")
    ingredient_two = Ingredient("presunto")
    assert ingredient_one.__eq__(ingredient_two) is True

    # def test_check_not_same_ingredient():
    ingredient_one = Ingredient("presunto")
    ingredient_two = Ingredient("ovo")
    assert ingredient_one.__eq__(ingredient_two) is False

    # def test_check_invalid_ingredient_restrictions_method():
    ingredient_x = Ingredient("x")
    assert ingredient_x.restrictions == set()
    assert ingredient_x.name == "x"

    # def test_check_valid_ingredient_representation_method():
    ingredient_shrimp = Ingredient("camarão")
    assert ingredient_shrimp.__repr__() == "Ingredient('camarão')"

    # def test_check_same_ingredient_hashes_not_equal():
    ingredient_other_shrimp = Ingredient("camarão")
    assert ingredient_shrimp.__hash__() == ingredient_other_shrimp.__hash__()

    # def test_check_differente_ingredient_hashes_not_equal():
    ingredient_egg = Ingredient("egg")
    assert ingredient_egg.__hash__() != ingredient_shrimp.__hash__()
