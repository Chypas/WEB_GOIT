-- Список курсів, які певному студенту читає певний викладач.

SELECT s.fullname, t.fullname, d.name AS course_name
FROM disciplines d
JOIN grades g ON g.discipline_id = d.id
JOIN students s ON s.id = g.student_id
JOIN teachers t ON t.id = d.teacher_id
WHERE s.id = 1 AND t.id = 1
GROUP BY d.name;