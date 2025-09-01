-- Select city id and name along with state information
-- Join cities and states tables to show complete city data with state context
-- Results sorted alphabetically by city name for easy reading
SELECT 
    cities.id,        
    cities.name,         
    states.name 
FROM cities
JOIN states
ORDER BY cities.name;                        
