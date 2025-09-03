-- Create a database named 'hbtn_0d_usa' if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create a table named 'states' if it doesn't already exist
-- The 'id' column is an integer, primary key, and automatically increments
-- The 'name' column is a variable-length string (up to 256 chars) and cannot be NULL
CREATE TABLE IF NOT EXISTS states (
    id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each state, auto-generated
    name VARCHAR(256) NOT NULL          -- State name, must always have a value
);
