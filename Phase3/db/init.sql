CREATE DATABASE knights;
use knights;

CREATE TABLE favorite_colors (
  name VARCHAR(20),
  color VARCHAR(10)
);

INSERT INTO favorite_colors
  (name, color)
VALUES
  ('Lancelot', 'blue'),
  ('Galahad', 'yellow');


CREATE TABLE publisher (
  name VARCHAR(20),
  topic VARCHAR(10)
);

INSERT INTO publisher
  (name, topic)
VALUES
  ('P1', 'BUSINESS'),
  ('P2', 'TECHNOLOGY');

CREATE TABLE subscriber (
  topic VARCHAR(10),
  name VARCHAR(20)
);

INSERT INTO subscriber
  (topic, name)
VALUES
  ('TECHNOLOGY', 'S1');