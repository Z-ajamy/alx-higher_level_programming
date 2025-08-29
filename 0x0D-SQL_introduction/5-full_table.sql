-- Query the MySQL information_schema to get detailed column information for a specific table
-- This provides more comprehensive metadata than the basic DESCRIBE command
-- Retrieves column details from the system's metadata tables
SELECT 
    COLUMN_NAME,        -- Name of each column in the table
    COLUMN_TYPE,        -- Full data type specification (e.g., 'int(11)', 'varchar(256)')
    IS_NULLABLE,        -- Whether the column accepts NULL values ('YES' or 'NO')
    COLUMN_KEY,         -- Key type: 'PRI' (primary), 'UNI' (unique), 'MUL' (multiple), or empty
    COLUMN_DEFAULT,     -- Default value assigned to the column (NULL if no default)
    EXTRA              -- Additional attributes like 'auto_increment', 'on update CURRENT_TIMESTAMP', etc.
FROM information_schema.COLUMNS
WHERE 
    TABLE_SCHEMA = 'hbtn_0c_0'     -- Filter for specific database name
    AND TABLE_NAME = 'first_table'; -- Filter for specific table name
