SELECT recclass, ROUND(AVG(CAST(mass AS FLOAT)),2) AS avg_mass
FROM Meteorites
GROUP BY recclass
ORDER BY avg_mass DESC