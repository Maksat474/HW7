import sqlite3

with sqlite3.connect('students.db') as conn:
    cursor = conn.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS student (
                id INTEGER PRIMARY KEY,
                hobby TEXT,
                name TEXT,
                surname TEXT,
                year_of_birth INTEGER,
                points_hw INTEGER
            )
        ''')

    students = [
        (1, 'Футбол', 'Максат', 'Конурбаев', 2004, 15),
        (2, 'Танцы', 'Жасмин', 'Маданбекова', 2005, 14),
        (3, 'Футбол', 'Сыймык', 'Шукуров', 2004, 12),
        (4, 'Легкая атлетика', 'Айтбек', 'Асыранбеков', 2005, 9),
        (5, 'Баскетбол', 'Стас', 'Ионов', 2004, 13),
        (6, 'Баскетбол', 'Данияр', 'Насиров', 2003, 6),
        (7, 'Борьба', 'Нурэл', 'Зухрапов', 2006, 8),
        (8, 'Футбол', 'Кубат', 'Сагынбеков', 2002, 10),
        (9, 'Футбол', 'Аскар', 'Тологонов', 2002, 10),
        (10, 'Теннис', 'Баатыр', 'Абакиров', 2003, 11)
    ]

    cursor.executemany('''
            INSERT INTO student (id, hobby, name, surname, year_of_birth, points_hw)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', students)

    cursor.execute('SELECT * FROM student WHERE LENGTH(surname) > 10')
    long_surnames = cursor.fetchall()

    cursor.execute('UPDATE student SET name = "genius" WHERE points_hw > 10')

    cursor.execute('SELECT * FROM student WHERE name = "genius"')
    genius_students = cursor.fetchall()

    cursor.execute('DELETE FROM student WHERE id % 2 = 0')