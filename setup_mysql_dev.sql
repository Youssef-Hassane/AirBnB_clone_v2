-- Create the database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create the database user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant all privileges on the database to the user
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
-- Grant select privilege on performance schema to the user
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
-- Flush privileges
FLUSH PRIVILEGES;
