-- Знайти середній бал на потоці (по всій таблиці оцінок).

SELECT d.name, ROUND(AVG(g.grade), 2) as avg_grade
FROM grades g
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN disciplines d ON d.id = g.discipline_id 
WHERE g.grade 
GROUP BY d.name
ORDER BY avg_grade DESC;