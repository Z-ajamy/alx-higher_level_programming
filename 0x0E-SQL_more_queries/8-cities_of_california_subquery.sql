SELECT id, name from cities where state_id all (
    SELECT id from states where name = California
);
