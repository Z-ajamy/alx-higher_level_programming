-- Select the id and name of cities
-- Only include cities where the 'state_id' matches the id of a state named "California"
SELECT id, name
FROM cities
WHERE state_id IN (
    -- Subquery: get all state IDs where the state name is "California"
    SELECT id
    FROM states
    WHERE states.name = "California"
);
