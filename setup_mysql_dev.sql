-- Create Database if not exists
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create User if doesnt exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges to the user on the db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privileges on performance_schema.
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
