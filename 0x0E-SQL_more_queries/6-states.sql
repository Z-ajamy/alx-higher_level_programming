-- Create a new database for USA-related data if it doesn't already exist
-- Safe creation pattern prevents errors on repeated execution
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to the newly created database for subsequent operations
-- All following table creations will be in this database context
USE hbtn_0d_usa;

-- Create a table to store US state information
-- SYNTAX ERROR: 'auto generated' should be 'AUTO_INCREMENT'
-- This table is designed to store state names with unique identifiers
CREATE TABLE IF NOT EXISTS states(
    id INT PRIMARY KEY AUTO_INCREMENT,  -- CORRECTED: Auto-incrementing unique identifier
    name VARCHAR(256) NOT NULL          -- State name, required field (cannot be NULL)
);
