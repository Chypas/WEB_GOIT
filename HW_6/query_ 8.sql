-- Знайти середній бал, який ставить певний викладач зі своїх предметів.

SELECT t.fullname, d.name, ROUND(AVG(g.grade), 2) as avg_grade 
FROM grades g
JOIN teachers t ON t.id = d.id 
JOIN disciplines d ON d.id = g.discipline_id
WHERE t.id AND d.id
GROUP BY t.fullname
ORDER BY avg_grade DESC;