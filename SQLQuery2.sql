SELECT recclass
FROM Meteorites
GROUP BY recclass
HAVING AVG(CAST(mass AS FLOAT)) < 5000


