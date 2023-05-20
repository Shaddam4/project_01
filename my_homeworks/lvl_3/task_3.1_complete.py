# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - использовать готовые классы numpy.array() и pandas.DataFrame() запрещено!
#   - проявите фантазию :)

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[None for j in range(cols)] for i in range(rows)]

    def set_value(self, row, cols, value):
        self.matrix[row][cols] = value

    def get_value(self, row, cols):
        return self.matrix[row][cols]

    def get_num_rows(self):
        return self.rows

    def get_num_cols(self):
        return self.cols

    def print_matrix(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.matrix[i][j], end=' ')
            print()


# Установка размера матрицы
m = Matrix(5, 5)

# Установка значений матрицы
m.set_value(0, 0, [1, 2, 7])
m.set_value(0, 1, 0)
m.set_value(0, 2, 3)
m.set_value(0, 3, 4)
m.set_value(1, 0, 5)
m.set_value(1, 1, 6)
m.set_value(1, 2, 7)
m.set_value(1, 3, 8)
m.set_value(2, 0, 9)
m.set_value(2, 1, 10)
m.set_value(2, 2, 11)
m.set_value(2, 3, 12)
print(m.get_num_rows()) # вывод количества строк
print(m.get_num_cols()) # вывод количества колонок
print(m.get_value(1, 2)) # вывод значения ячейки (строка, колонка)

m.print_matrix() # output: