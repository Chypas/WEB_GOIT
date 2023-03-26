-- Середній бал, який певний викладач ставить певному студентові.

SELECT s.fullname AS Student, t.fullname AS Teacher, d.name AS Didcepline, ROUND(AVG(g.grade), 2) as "Average grade"
FROM grades g
JOIN disciplines d ON d.id = g.discipline_id
JOIN teachers t ON t.id = d.teacher_id
JOIN students s ON s.id = g.student_id
WHERE t.id = 1 AND s.id = 1;