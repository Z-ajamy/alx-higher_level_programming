-- Goal of this query:
-- Show all TV shows (from tv_shows) and their associated genres (if any).
-- Unlike INNER JOIN, a LEFT JOIN ensures that shows with no genres still appear.

SELECT 
    tv_shows.title AS title,             -- First column: the TV show's title
    tv_show_genres.genre_id AS genre_id  -- Second column: the genre identifier (NULL if no genre)
FROM tv_shows
    -- Start with the 'tv_shows' table (all shows will be included)

LEFT JOIN tv_show_genres
    ON tv_show_genres.show_id = tv_shows.id
    -- Use LEFT JOIN so that even shows without genres will still appear
    -- If a show has no matching entry in 'tv_show_genres',
    -- the genre_id column will return NULL

ORDER BY 
    title,      -- Order alphabetically by TV show title
    genre_id;   -- Then by genre_id (NULLs appear last by default)
