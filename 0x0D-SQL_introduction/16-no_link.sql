-- Retrieve score and name columns for records with non-empty names
-- Filters out any rows where the name field is an empty string
-- Results sorted alphabetically by name, then by highest scores first
SELECT score, name 
FROM second_table 
WHERE name != ""         -- Filter: exclude records with empty string names (but allows NULL)
ORDER BY score DESC;     -- Secondary sort: highest scores first within each name group
