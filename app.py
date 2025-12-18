from lib.database_connection import DatabaseConnection
from lib.recipe import Recipe
from lib.recipe_repository import RecipeRepository

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")

    def run(self):
        recipe_repo = RecipeRepository(self._connection)
        recipes = recipe_repo.all()
        for recipe in recipes:
            print(f"Recipe: {recipe.name}")


if __name__ == '__main__':
    app = Application()
    app.run()
