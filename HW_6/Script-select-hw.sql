--������ 5 �������� �� ��������� ������� ����� � ��� ��������

SELECT s.fullname, ROUND(AVG(g.grade), 2) as avg_grade
FROM grades g
LEFT JOIN students s ON s.id = g.student_id
GROUP BY s.id 
ORDER BY avg_grade DESC
LIMIT 5;

-- ������ �������� �� �������� ������� ����� � ������� ��������.

SELECT d.name, s.fullname, ROUND(AVG(g.grade), 2) as avg_grade
FROM grades g
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN disciplines d ON d.id = g.discipline_id 
WHERE d.id = 1
GROUP BY s.id
ORDER BY avg_grade DESC
LIMIT 1;

-- ������ ������� ��� � ������ � ������� ��������.

SELECT gr.name, d.name, ROUND(AVG(g.grade), 2) as avg_grade
FROM grades g
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN disciplines d ON d.id = g.discipline_id
LEFT JOIN [groups] gr ON s.group_id = gr.id  
WHERE d.id = 1
GROUP BY gr.id
ORDER BY avg_grade DESC;

-- ������ ������� ��� �� ������ (�� ��� ������� ������).

SELECT d.name, ROUND(AVG(g.grade), 2) as avg_grade
FROM grades g
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN disciplines d ON d.id = g.discipline_id 
WHERE g.grade 
GROUP BY d.name
ORDER BY avg_grade DESC;

-- ������ �� ����� ���� ������ ��������.

SELECT t.fullname, d.name
FROM disciplines d  
LEFT JOIN teachers t ON d.teacher_id = t.id
WHERE t.id = 1;

-- ������ ������ �������� � ����� ����.

SELECT s.fullname, g.name 
FROM students s
LEFT JOIN groups g ON s.group_id = g.id
WHERE g.id = 1;

-- ������ ������ �������� � ������ ���� � ������� ��������.

SELECT s.fullname, gr.name, d.name, g.grade
FROM students s
LEFT JOIN grades g ON s.id = g.student_id
LEFT JOIN disciplines d ON g.discipline_id = d.id
LEFT JOIN groups gr ON s.group_id = gr.id
WHERE gr.id = 1 AND d.id = 1;

-- ������ ������� ���, ���� ������� ������ �������� � ���� ��������.

SELECT t.fullname, d.name, ROUND(AVG(g.grade), 2) as avg_grade 
FROM grades g
JOIN teachers t ON t.id = d.id 
JOIN disciplines d ON d.id = g.discipline_id
WHERE t.id AND d.id
GROUP BY t.fullname
ORDER BY avg_grade DESC;

-- ������ ������ �����, �� ����� �������.

SELECT s.fullname, d.name AS course_name
FROM disciplines d
JOIN grades g ON g.discipline_id = d.id
JOIN students s ON s.id = g.student_id
WHERE s.id = 1
GROUP BY d.name;

-- ������ �����, �� ������� �������� ���� ������ ��������.

SELECT s.fullname, t.fullname, d.name AS course_name
FROM disciplines d
JOIN grades g ON g.discipline_id = d.id
JOIN students s ON s.id = g.student_id
JOIN teachers t ON t.id = d.teacher_id
WHERE s.id = 1 AND t.id = 1
GROUP BY d.name;

-- ������� ���, ���� ������ �������� ������� ������� ���������.

SELECT s.fullname AS Student, t.fullname AS Teacher, d.name AS Didcepline, ROUND(AVG(g.grade), 2) as "Average grade"
FROM grades g
JOIN disciplines d ON d.id = g.discipline_id
JOIN teachers t ON t.id = d.teacher_id
JOIN students s ON s.id = g.student_id
WHERE t.id = 1 AND s.id = 1;

-- ������ �������� � ����� ���� � ������� �������� �� ���������� ������.

--SELECT students.fullname AS Student, AVG(grades.grade) AS avg_grade
--FROM grades
--JOIN disciplines ON grades.discipline_id = disciplines.id
--JOIN teachers ON teachers.id = disciplines.teacher_id
--JOIN students ON students.id = grades.student_id
--WHERE groups.id = 1 AND disciplines.id = 1;

