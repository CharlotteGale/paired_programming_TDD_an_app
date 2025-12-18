DROP TABLE IF EXISTS recipes;

CREATE TABLE recipes (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  cooking_time INT,
  rating INT
);