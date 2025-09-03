-- Create a table named 'cities' if it doesn't already exist
-- The 'id' column is an integer, primary key, and automatically increments
-- The 'state_id' column references the 'id' column in the 'states' table (foreign key)
-- The 'name' column is a variable-length string (up to 256 chars) and cannot be NULL
CREATE TABLE IF NOT EXISTS cities (
    id INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each city, auto-generated
    state_id INT,                          -- References a state from the 'states' table
    name VARCHAR(256) NOT NULL,            -- City name, must always have a value
    FOREIGN KEY (state_id) REFERENCES states(id)  -- Define foreign key relationship
);
