CREATE SCHEMA IF NOT EXISTS Core_Schema;
-- -----------------------------------------------------
-- Table 'Core_Schema'.'users'
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Core_Schema.users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(64) NULL DEFAULT NULL,
  username VARCHAR(64) NULL DEFAULT NULL,
  password_hash VARCHAR(128) NULL DEFAULT NULL,
  confirmed BOOLEAN DEFAULT FALSE
  );
-- -----------------------------------------------------
-- Table Core_Schema.heroes
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Core_Schema.heroes (
   Hero_ID SERIAL PRIMARY KEY ,
   Name VARCHAR(128)
   );

-- Load heroes data
COPY Core_Schema.heroes
FROM '/docker-entrypoint-initdb.d/heroes.csv' 
DELIMITER ','
CSV HEADER;
-- -----------------------------------------------------
-- Table 'Core_Schema'.'items'
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Core_Schema.items (
   Item_ID SERIAL PRIMARY KEY ,
   Name VARCHAR(128)
   );

-- Load item data
COPY Core_Schema.items
FROM '/docker-entrypoint-initdb.d/items.csv' 
DELIMITER ','
CSV HEADER;
