# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

# import sqlite3
#
# connection = sqlite3.connect('teatchers.db')
# cursor = connection.cursor()
# query = """CREATE TABLE Students
# (
# Students_Id INTEGER NOT NULL,
# Students_Name TEXT NOT NULL,
# School_Id INTEGER NOT NULL PRIMARY KEY
# );
# """
# cursor.execute(query)
# connection.commit()
# connection.close()
#
# connection = sqlite3.connect('teatchers.db')
# cursor = connection.cursor()
# query = """INSERT INTO Students (Students_Id, Students_Name, School_Id)
# VALUES
# ('201', 'Иван', 1),
# ('202', 'Петр', 2),
# ('203', 'Анастасия', 3),
# ('204', 'Игорь', 4);
# """
# cursor.execute(query)
# connection.commit()
# connection.close()


import sqlite3


def get_connection():
    connection = sqlite3.connect('teatchers.db')
    return connection


def close_connection(connection):
    if connection:
        connection.close()


def get_student_detail(student_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    select_query = '''
    SELECT Students.Students_Id,
    Students.Students_Name,
    Students.School_Id,
    School.School_Name
    FROM Students JOIN School ON Students.School_Id = School.School_Id WHERE students_id = ?;'''
    cursor.execute(select_query, (student_id,))
    record = cursor.fetchone()
    close_connection(connection)
    print("Получение информации о студенте  по его ID")
    print("ID Студента:", record[0])
    print("Имя студента:", record[1])
    print("ID школы:", record[2])
    print("Название школы:", record[3])
  except (Exception, sqlite3.Error) as error:
    print('Ошибка в получении данных:', error)


id_s = input("Введите id студента: ")
get_student_detail(id_s)