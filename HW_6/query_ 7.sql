-- Знайти оцінки студентів у окремій групі з певного предмета.

SELECT s.fullname, gr.name, d.name, g.grade
FROM students s
LEFT JOIN grades g ON s.id = g.student_id
LEFT JOIN disciplines d ON g.discipline_id = d.id
LEFT JOIN groups gr ON s.group_id = gr.id
WHERE gr.id = 1 AND d.id = 1;