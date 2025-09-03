-- Goal of this query:
-- Display all TV shows (from tv_shows) along with their associated genres (by genre_id).
-- This helps us know which genres each show belongs to.
-- The results are sorted alphabetically by show title and then by genre_id.

SELECT 
    tv_shows.title AS title,             -- First column: the TV show's title
    tv_show_genres.genre_id AS genre_id  -- Second column: the genre identifier linked to the show
FROM tv_shows
    -- Start from the 'tv_shows' table which contains all shows

JOIN tv_show_genres 
    ON tv_show_genres.show_id = tv_shows.id
    -- Perform an INNER JOIN with the 'tv_show_genres' table
    -- Condition: the show_id in 'tv_show_genres' must match the id in 'tv_shows'
    -- This links each show to all of its genres

ORDER BY 
    title,      -- First, order alphabetically by the show's title
    genre_id;   -- Then, order by genre_id in ascending order
