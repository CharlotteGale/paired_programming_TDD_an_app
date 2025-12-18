from lib.recipe_repository import RecipeRepository
from lib.recipe import Recipe

def test_get_all_recipe_records(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repo = RecipeRepository(db_connection)

    recipes = repo.all()
    
    assert recipes == [
        Recipe(1, 'Spaghetti Carbonara', 20, 5),
        Recipe(2, 'Chicken Stir-Fry', 15, 4),
        Recipe(3, 'Vegetable Curry', 35, 4),
        Recipe(4, 'Cheese Omelette', 10, 3),
        Recipe(5, 'Beef Tacos', 25, 5),
        Recipe(6, 'Margherita Pizza', 45, 5),
        Recipe(7, 'Tomato Soup', 30, 4),
        Recipe(8, 'Grilled Salmon', 20, 5),
        Recipe(9, 'Pad Thai', 25, 5),
        Recipe(10,'Chocolate Brownies', 30, 5)
    ]
    
def test_get_single_recipe_record(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repo = RecipeRepository(db_connection)

    recipe = repo.find(1)

    assert recipe == Recipe(1, 'Spaghetti Carbonara', 20, 5)