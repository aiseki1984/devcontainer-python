CREATE TABLE books
(
  id SERIAL NOT NULL PRIMARY KEY,
  title VARCHAR(100),
  insert_timestamp TIMESTAMP DEFAULT NULL
);