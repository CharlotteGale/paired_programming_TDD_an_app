_Copy this recipe template to design and create a database table from a specification._

## 1. Extract nouns from the user stories or specification

> As a food lover,      
> So I can stay organised and decide what to cook,      
> I'd like to keep a list of all my recipes with their names.

> As a food lover,      
> So I can stay organised and decide what to cook,      
> I'd like to keep the average cooking time (in minutes) for each recipe.

> As a food lover,      
> So I can stay organised and decide what to cook,      
> I'd like to give a rating to each of the recipes (from 1 to 5).


```
Nouns:

recipes, names, cooking time, rating
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties                 |
| --------------------- | -------------------------- |
| recipes              | name, cooking_time, rating |

Name of the table (always plural): `recipes`

Column names: `name`, `cooking_time`, `rating`

## 3. Decide the column types

```bash

id: SERIAL
name: text
cooking_time: int | varchar
rating: int
```

## 4. Write the SQL

```sql
-- EXAMPLE
-- file: seeds/recipes.sql

-- Replace the table name, column names and types.

CREATE TABLE recipes (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  cooking_time INT,
  rating INT
);
```

## 5. Create the table

```bash
psql -h 127.0.0.1 recipes < recipes.sql
```

## 3. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by `Repository` for the Repository class name.

```python
# EXAMPLE
# Table name: recipes

# Model class
# (in lib/recipe.py)
class Recipes

    def __init__(self, id, name, cooking_time, rating)
        '''
        parameters - id(None) ,name(string), cooking_time(int), rating(int)
        outputs - nothing
        side effects - sets all parameters as instance variables
        '''
    def __eq__(self, other):
        '''
        params - other(class object)
        outputs - Bool, doesn't dirrectly output, but is returned
        side effect - nothing
        '''
    def __repr__(self):
        '''
        params - nothing
        outputs - formats the class object as string
        side effect - nothing
        '''

# Repository class
# (in lib/recipe_repository.py)
class RecipeRepository

    def __init__(self, connection)
        '''
        params - connection
        outputs - nothing
        side effect - essablishes the connection to the database.
        '''

    def all(self):
        '''
        params - nothing
        outputs - List of dictionarys(recipes)
        side effect - nothing
        '''     

    def find(self, id):
        '''
        params - id(int)
        outputs - a single class objec with the specified id
        side effect - nothing
        '''     

```

## 6. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

```python
# EXAMPLES
# test_recip_repo_.py
# 1
# Get all recipe

repo = RecipeRepository()

recipe = repo.all()

len(recipe) # =>  2

recipe[0].id # =>  1
recipe[0].name # =>  'test'
recipe[0].cooking_time # =>  5
recipe[0].rating # => 5

recipe[1].id # =>  2
recipe[1].name # =>  'test aswell'
recipe[1].cooking_time # =>  10
recipe[1].rating # => 1

# 2
# Get a single recipe

repo = RecipeRepository()

recipe = repo.find(1)

recipe.id # =>  1
recipe.name # =>  'test'
recipe.cooking_time # =>  5
recipe.rating # => 5

#test_recipe.py

#1
# recipe constructs correctly

recipe = Recipes(['id'], ['name'], ['cooking_time'], ['rating'])

recipe.id = id
recipe.name = name
recipe.cooking_time = cooking_time
recipe.rating = rating

#2
# check if identical recipes are equal

recipe1 = Recipes(['id'], ['name'], ['cooking_time'], ['rating'])
recipe2 = Recipes(['id'], ['name'], ['cooking_time'], ['rating'])

recipe1 == recipe2 # => True

#3
#check if format is nice

recipe = Recipes(['id'], ['name'], ['cooking_time'], ['rating'])

str(recipe) == 'Recipes([id], [name], [cooking_time], [rating])'
```

Encode this example as a test.


## 7. Test-drive and implement the Repository class behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._