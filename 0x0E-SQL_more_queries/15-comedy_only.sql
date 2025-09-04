-- Goal:
-- Retrieve all TV shows that are classified under the genre "Comedy"

SELECT 
    tv_shows.title            -- Select the title of the TV show
FROM tv_shows
    -- Start with the list of all shows

JOIN tv_show_genres 
    ON tv_shows.id = tv_show_genres.show_id
    -- Join the bridge table (tv_show_genres)
    -- Match the show id with show_id in the bridge table

JOIN tv_genres 
    ON tv_genres.id = tv_show_genres.genre_id
    -- Join the genres table to access genre names
    -- Match genre_id from the bridge table with the id in tv_genres

WHERE tv_genres.name = "Comedy"
    -- Filter so we only keep shows that have the genre "Comedy"

ORDER BY tv_shows.title;
    -- Sort the resulting show titles alphabetically
