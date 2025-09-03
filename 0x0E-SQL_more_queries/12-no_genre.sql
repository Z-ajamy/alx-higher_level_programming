-- Goal of this query:
-- Show all TV shows that have NO genres linked to them.
-- We use LEFT JOIN + WHERE genre_id IS NULL to filter those shows.

SELECT 
    tv_shows.title AS title,             -- TV show title
    tv_show_genres.genre_id AS genre_id  -- This will be NULL because no genre is linked
FROM tv_shows
LEFT JOIN tv_show_genres 
    ON tv_show_genres.show_id = tv_shows.id
    -- LEFT JOIN keeps all shows, even if no genres exist

WHERE tv_show_genres.genre_id IS NULL
    -- Filter: only keep shows that have no genres (unmatched rows)

ORDER BY 
    title,      -- Sort results alphabetically by show title
    genre_id;   -- genre_id will always be NULL here, but kept for syntax consistency
