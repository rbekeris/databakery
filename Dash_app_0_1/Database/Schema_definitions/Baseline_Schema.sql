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
   id SERIAL PRIMARY KEY ,
   name VARCHAR(128),
   localized_name VARCHAR(128),
   primary_attr VARCHAR(128),
   attack_type VARCHAR(128),
   --each hero can have a list of roles, thus we need to use an array type
   roles VARCHAR[]);

-- -----------------------------------------------------
-- Table 'Core_Schema'.'items'
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Core_Schema.items (
   Item_ID SERIAL PRIMARY KEY ,
   Name VARCHAR(128)
   );

CREATE TABLE IF NOT EXISTS Core_Schema.steam_accounts (
  id SERIAL PRIMARY KEY,
  Steam32_ID bigint NULL DEFAULT NULL,
  Steam64_ID bigint NULL DEFAULT NULL,
  Steam_Nick_Name VARCHAR NULL DEFAULT NULL,
  user_id SERIAL,
  CONSTRAINT fk_user_id
      FOREIGN KEY(user_id) 
	  REFERENCES Core_Schema.users(id)
	  ON DELETE SET NULL
  );

-- Load item data
COPY Core_Schema.items
FROM '/docker-entrypoint-initdb.d/items.csv' 
DELIMITER ','
CSV HEADER;

