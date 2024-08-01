-- Create the table 'unique_id' if it does not already exist
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1,
    name VARCHAR(256),
    CONSTRAINT unique_id_unique UNIQUE (id)
);
