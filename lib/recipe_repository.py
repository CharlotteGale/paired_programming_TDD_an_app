from lib.recipe import Recipe

class RecipeRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        pass