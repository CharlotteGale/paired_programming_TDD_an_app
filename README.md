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
# Table name: students

# Model class
# (in lib/student.py)
class Student


# Repository class
# (in lib/student_repository.py)
class StudentRepository

```

## 4. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

```python
# EXAMPLE
# Table name: students

# Model class
# (in lib/student.py)

class Student:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.cohort_name = ""

        # Replace the attributes by your own columns.


# We can set the attributes to default empty values and set them later,
# here's an example:
#
# >>> student = Student()
# >>> student.name = "Will"
# >>> student.cohort_name = "September Devs"
# >>> student.name
# 'Will'
# >>> student.cohort_name
# 'September Devs'

```

## 5. Define the Repository Class interface

Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

```python
# EXAMPLE
# Table name: students

# Repository class
# (in lib/student_repository.py)

class StudentRepository():

    # Selecting all records
    # No arguments
    def all():
        # Executes the SQL query:
        # SELECT id, name, cohort_name FROM students;

        # Returns an array of Student objects.

        # Gets a single record by its ID
        # One argument: the id (number)
    def find(id):
        # Executes the SQL query:
        # SELECT id, name, cohort_name FROM students WHERE id = $1;

        # Returns a single Student object.

        # Add more methods below for each operation you'd like to implement.

    # def create(student)
    # 

    # def update(student)
    # 

    # def delete(student)
    # 

```

## 6. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

```python
# EXAMPLES

# 1
# Get all students

repo = StudentRepository()

students = repo.all()

len(students) # =>  2

students[0].id # =>  1
students[0].name # =>  'David'
students[0].cohort_name # =>  'April 2022'

students[1].id # =>  2
students[1].name # =>  'Anna'
students[1].cohort_name # =>  'May 2022'

# 2
# Get a single student

repo = StudentRepository()

student = repo.find(1)

student.id # =>  1
student.name # =>  'David'
student.cohort_name # =>  'April 2022'

# Add more examples for each method
```

Encode this example as a test.


## 7. Test-drive and implement the Repository class behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._