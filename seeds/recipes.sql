DROP TABLE IF EXISTS recipes;

CREATE TABLE recipes (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  cooking_time INT,
  rating INT
);

INSERT INTO recipes (name, cooking_time, rating) 
    VALUES
        ('Spaghetti Carbonara', 20, 5),
        ('Chicken Stir-Fry', 15, 4),
        ('Vegetable Curry', 35, 4),
        ('Cheese Omelette', 10, 3),
        ('Beef Tacos', 25, 5),
        ('Margherita Pizza', 45, 5),
        ('Tomato Soup', 30, 4),
        ('Grilled Salmon', 20, 5),
        ('Pad Thai', 25, 5),
        ('Chocolate Brownies', 30, 5);