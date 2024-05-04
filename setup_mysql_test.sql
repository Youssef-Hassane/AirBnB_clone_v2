-- Create the database for the project if it does not exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create a user for the test database
-- This user will be used to connect to the database during testing
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant all privileges on the test database to the test user
-- This allows the user to perform any operation on the test database
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
-- Grant select privilege on performance schema to the test user
-- This is required for the test user to access performance data of the test database
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
-- Flush privileges to apply the changes
FLUSH PRIVILEGES;

