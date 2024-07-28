-- gdfgdf f gfg dfdfgr f fdg df fd gdfg dg fd 
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
