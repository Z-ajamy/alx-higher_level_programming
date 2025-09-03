-- Select the id of the city, its name, and the corresponding state name
-- Join 'cities' with 'states' using the foreign key relationship
SELECT 
    cities.id, 
    cities.name AS name,     -- Alias for city name
    states.name AS name     -- Alias for state name
FROM cities
JOIN states ON states.id = cities.state_id;
