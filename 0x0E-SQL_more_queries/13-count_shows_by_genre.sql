-- Goal of this query:
-- Show each genre and the number of shows that belong to it.
-- We join the genres table with the linking table (tv_show_genres).
-- Then we group by genre and count the shows.

SELECT 
    tv_genres.name AS genre,              -- The genre name (e.g., Comedy, Drama)
    COUNT(tv_show_genres.show_id) AS number_of_shows  -- How many shows belong to this genre
FROM tv_show_genres
JOIN tv_genres 
    ON tv_show_genres.genre_id = tv_genres.id
    -- Join 'tv_show_genres' (bridge table) with 'tv_genres' (genre names)

GROUP BY 
    tv_genres.name
    -- Group results by genre so COUNT() works per genre

ORDER BY 
    number_of_shows DESC;
