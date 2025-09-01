-- Create a new database for USA-related data if it doesn't already exist
-- Safe creation pattern prevents errors on repeated execution
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to the newly created database for subsequent operations
-- All following table creations will be in this database context
USE hbtn_0d_usa;

-- Create a table to store US cities with references to their states
-- SYNTAX ERROR: 'refrences' should be 'REFERENCES' and 'INT' shouldn't be in the reference
-- This table links cities to states through a foreign key relationship
CREATE TABLE IF NOT EXISTS cities (
    id INT PRIMARY KEY AUTO_INCREMENT,  -- Auto-incrementing unique identifier for each city
    state_id INT NOT NULL,               -- Foreign key linking to states table (required)
    FOREIGN KEY (state_id) REFERENCES states(id),  -- CORRECTED: Proper foreign key syntax
    name VARCHAR(256) NOT NULL           -- City name, required field (cannot be NULL)
);
