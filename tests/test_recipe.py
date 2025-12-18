from lib.recipe import Recipe

def test_recipe_constucts():
    recipe = Recipe(1, 'test', 10, 1)
    
    assert recipe.id == 1
    assert recipe.name == 'test'
    assert recipe.cooking_time == 10
    assert recipe.rating == 1
def test_recipes_are_equal():
    recipe1 = Recipe(1, 'test', 10, 1)
    recipe2 = Recipe(1, 'test', 10, 1)
    
    assert recipe1 == recipe2
def test_format_recipe_as_string():
    recipe = Recipe(1, 'test', 10, 1)
    
    assert str(recipe) == 'Recipe(1, test, 10, 1)'