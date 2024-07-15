-- Create a Database if not exists
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create a User if not exists
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant the user all privileges on hbnh_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege to performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
