-- Create a database named 'hbtn_0d_usa' if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Select the 'hbtn_0d_usa' database for use
USE hbtn_0d_usa;

-- Create a table named 'cities' if it doesn't already exist
-- 'id' is the primary key, auto-incremented integer
-- 'state_id' is a required column (NOT NULL) that references 'states.id'
-- 'name' is a required string column with max length 256 characters
CREATE TABLE IF NOT EXISTS cities (
    id INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each city
    state_id INT NOT NULL,                   -- Must reference a valid state (cannot be NULL)
    name VARCHAR(256) NOT NULL,              -- City name (cannot be NULL)
    FOREIGN KEY (state_id) REFERENCES states(id)  -- Foreign key linking city to a state
);
