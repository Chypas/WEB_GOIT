-- Знайти які курси читає певний викладач.

SELECT t.fullname, d.name
FROM disciplines d  
LEFT JOIN teachers t ON d.teacher_id = t.id
WHERE t.id = 1;