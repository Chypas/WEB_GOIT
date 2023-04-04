from sqlalchemy import func, desc, select, and_

from database.models import Teacher, Student, Discipline, Grade, Group
from database.db import session


def select_1():
    """
    Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    SELECT s.fullname, ROUND(AVG(g.grade), 2) as avg_grade
    FROM grades g
    LEFT JOIN students s ON s.id = g.student_id
    GROUP BY s.id
    ORDER BY avg_grade DESC
    LIMIT 5;
    :return:
    """
    result = session.query(
        Student.fullname,
        func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade) \
        .join(Student) \
        .group_by(Student.id) \
        .order_by(desc('avg_grade')).limit(5).all() \
        # .order_by(Grade.grade.desc())
    return result


def select_2():
    """
    SELECT d.name, s.fullname, ROUND(AVG(g.grade), 2) as avg_grade
    FROM grades g
    LEFT JOIN students s ON s.id = g.student_id
    LEFT JOIN disciplines d ON d.id = g.discipline_id
    WHERE d.id = 5
    GROUP BY s.id
    ORDER BY avg_grade DESC
    LIMIT 1;
    :return:
    """
    result = session.query(
        Discipline.name,
        Student.fullname,
        func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).join(Discipline) \
        .filter(Discipline.id == 5) \
        .group_by(Student.id, Discipline.name).order_by(desc('avg_grade')).limit(1).first()
    return result


def select_3():
    # Знайти середній бал у групах з певного предмета.
    # SELECT gr.name, d.name, ROUND(AVG(g.grade), 2) as avg_grade
    # FROM grades g
    # LEFT JOIN students s ON s.id = g.student_id
    # LEFT JOIN disciplines d ON d.id = g.discipline_id
    # LEFT JOIN [groups] gr ON s.group_id = gr.id
    # WHERE d.id = 1
    # GROUP BY gr.id
    # ORDER BY avg_grade DESC;
    result = session.query(
        Group.name,
        Discipline.name,
        func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).join(Discipline).join(Group) \
        .filter(Discipline.id == 1).group_by(Group.id).group_by(Discipline.name).order_by(desc('avg_grade')).all()
    return result


def select_4():
    # Знайти середній бал на потоці (по всій таблиці оцінок).
    # SELECT d.name, ROUND(AVG(g.grade), 2) as avg_grade
    # FROM grades g
    # LEFT JOIN students s ON s.id = g.student_id
    # LEFT JOIN disciplines d ON d.id = g.discipline_id
    # WHERE g.grade
    # GROUP BY d.name
    # ORDER BY avg_grade DESC;
    result = session.query(
        Discipline.name,
        func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).join(Discipline) \
        .group_by(Discipline.name).order_by(desc('avg_grade')).all()
    return result


def select_5():
    # Знайти які курси читає певний викладач.
    # SELECT t.fullname, d.name
    # FROM disciplines d
    # LEFT JOIN teachers t ON d.teacher_id = t.id
    # WHERE t.id = 1;
    result = session.query(
        Discipline.name,
        Teacher.fullname) \
        .select_from(Discipline).join(Teacher) \
        .filter(Teacher.id == 2).all()
    return result


def select_6():
    # Знайти список студентів у певній групі.
    # SELECT s.fullname, g.name
    # FROM students s
    # LEFT JOIN groups g ON s.group_id = g.id
    # WHERE g.id = 1;
    result = session.query(
        Student.fullname,
        Group.name) \
        .select_from(Student).join(Group) \
        .filter(Group.id == 1).all()
    return result


def select_7():
    # Знайти оцінки студентів у окремій групі з певного предмета.
    # SELECT s.fullname, gr.name, d.name, g.grade
    # FROM students s
    # LEFT JOIN grades g ON s.id = g.student_id
    # LEFT JOIN disciplines d ON g.discipline_id = d.id
    # LEFT JOIN groups gr ON s.group_id = gr.id
    # WHERE gr.id = 1 AND d.id = 1;
    result = session.query(
        Group.name,
        Student.fullname,
        Grade.grade,
        Discipline.name) \
        .select_from(Grade).join(Student).join(Group).join(Discipline) \
        .filter(Group.id == 1, Discipline.id == 1).order_by(desc(Student.fullname)).all()
    return result


def select_8():
    # Знайти середній бал, який ставить певний викладач зі своїх предметів.
    # SELECT t.fullname, d.name, ROUND(AVG(g.grade), 2) as avg_grade
    # FROM grades g
    # JOIN teachers t ON t.id = d.id
    # JOIN disciplines d ON d.id = g.discipline_id
    # WHERE t.id AND d.id
    # GROUP BY t.fullname
    # ORDER BY avg_grade DESC;
    result = session.query(
        Teacher.fullname,
        Discipline.name,
        func.round(func.avg(Grade.grade), 2)) \
        .select_from(Discipline).join(Grade).join(Teacher) \
        .group_by(Teacher.fullname). group_by(Discipline.name).all()
    return result


def select_9():
    # Знайти список курсів, які відвідує студент.
    # SELECT s.fullname, d.name AS course_name
    # FROM disciplines d
    # JOIN grades g ON g.discipline_id = d.id
    # JOIN students s ON s.id = g.student_id
    # WHERE s.id = 1
    # GROUP BY d.name;
    result = session.query(
        Student.fullname,
        Discipline.name) \
        .select_from(Discipline).join(Grade).join(Student) \
        .filter(Student.id == 1).group_by(Student.fullname).group_by(Discipline.name).all()
    return result


def select_10():
    # Список курсів, які певному студенту читає певний викладач.
    # SELECT s.fullname, t.fullname, d.name AS course_name
    # FROM disciplines d
    # JOIN grades g ON g.discipline_id = d.id
    # JOIN students s ON s.id = g.student_id
    # JOIN teachers t ON t.id = d.teacher_id
    # WHERE s.id = 1 AND t.id = 1
    # GROUP BY d.name;
    result = session.query(
        Student.fullname,
        Teacher.fullname,
        Discipline.name) \
        .select_from(Discipline).join(Grade).join(Student).join(Teacher) \
        .filter(Student.id == 20, Teacher.id == 2).group_by(Student.fullname).group_by(Discipline.name) \
        .group_by(Teacher.fullname).all()
    return result


def select_11():
    # Середній бал, який певний викладач ставить певному студентові.
    # SELECT s.fullname AS Student, t.fullname AS Teacher, d.name AS Discipline,
    # ROUND(AVG(g.grade), 2) as "Average grade"
    # FROM grades g
    # JOIN disciplines d ON d.id = g.discipline_id
    # JOIN teachers t ON t.id = d.teacher_id
    # JOIN students s ON s.id = g.student_id
    # WHERE t.id = 1 AND s.id = 1;
    result = session.query(
        Student.fullname,
        Teacher.fullname,
        Discipline.name,
        func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Discipline).join(Student).join(Teacher) \
        .filter(Student.id == 20, Teacher.id == 2).group_by(Student.fullname).group_by(Discipline.name) \
        .group_by(Teacher.fullname).all()
    return result


def select_12():
    """
    -- Оцінки студентів у певній групі з певного предмета на останньому занятті.
    select s.id, s.fullname, g.grade, g.date_of
    from grades g
    join students s on s.id = g.student_id
    where g.discipline_id = 3 and s.group_id = 3 and g.date_of = (
        select max(date_of)
        from grades g2
        join students s2 on s2.id = g2.student_id
        where g2.discipline_id = 3 and s2.group_id = 3
    );
    :return:
    """
    subquery = (select(func.max(Grade.date_of)).join(Student).filter(and_(
        Grade.discipline_id == 3, Student.group_id == 3
    )).scalar_subquery())

    result = session.query(Student.id, Student.fullname, Grade.grade, Grade.date_of) \
        .select_from(Grade) \
        .join(Student) \
        .filter(and_(Grade.discipline_id == 3, Student.group_id == 3, Grade.date_of == subquery)).all()
    return result


if __name__ == '__main__':
    print(select_11())
    # print(select_two())
    # print(select_12())
