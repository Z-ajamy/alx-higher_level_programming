-- Goal:
-- Retrieve all genre names that belong to the TV show "Dexter"

SELECT 
    tv_genres.name          -- Select the genre name (e.g., Drama, Thriller, Crime)
FROM tv_shows
    -- Start from the tv_shows table (contains all shows)

JOIN tv_show_genres 
    ON tv_shows.id = tv_show_genres.show_id
    -- Join the bridge table (tv_show_genres) that links shows to genres
    -- Condition: match the show id with the show_id in the bridge table

JOIN tv_genres 
    ON tv_show_genres.genre_id = tv_genres.id
    -- Join the genres table to get the actual genre names
    -- Condition: match genre_id from bridge table with id in tv_genres

WHERE tv_shows.title = "Dexter"
    -- Filter only the rows for the show with title = "Dexter"

ORDER BY tv_genres.name;
    -- Sort the resulting genres alphabetically
