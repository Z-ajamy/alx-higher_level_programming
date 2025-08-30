-- Retrieve score and name columns sorted by name alphabetically, then by score descending
-- Primary sort: names in alphabetical order (A to Z)
-- Secondary sort: when names are the same, highest scores appear first
-- This creates an alphabetical list with best scores shown first for each name
SELECT score, name 
FROM second_table 
ORDER BY name,           -- Primary sort: alphabetical order by name (ASC is default)
         score DESC;     -- Secondary sort: highest scores first within each name group
