-- Select all cities in California, ordered by city id
SELECT id, name
FROM cities
WHERE state_id = (
    -- Subquery to find the state_id for California
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;
