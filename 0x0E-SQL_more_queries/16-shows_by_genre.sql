-- Goal:
-- Retrieve all TV shows along with their genres (if any).
-- Using LEFT JOIN ensures that shows without genres are also included.

SELECT 
    tv_shows.title,        -- The TV show title
    tv_genres.name         -- The genre name (NULL if no genre is linked)
FROM tv_shows
    -- Start from the list of all shows

LEFT JOIN tv_show_genres 
    ON tv_shows.id = tv_show_genres.show_id
    -- Left join with the bridge table (tv_show_genres)
    -- If a show has no genres, it still appears but with NULLs for genre info

LEFT JOIN tv_genres 
    ON tv_genres.id = tv_show_genres.genre_id
    -- Left join with the genres table to fetch genre names
    -- If no match, genre_name will be NULL

ORDER BY 
    tv_shows.title,        -- Sort alphabetically by show title first
    tv_genres.name;        -- Then sort genres alphabetically per show
