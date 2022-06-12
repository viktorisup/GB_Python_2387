# Реализовать класс Matrix (матрица).

class Matrix:
    def __init__(self, matrix_lst):
        self.matrix_lst = matrix_lst

    def __str__(self):
        str1 = ''
        if len(self.matrix_lst) == 3 and len(self.matrix_lst[0]) == 3 and len(self.matrix_lst[1]) == 3\
                and len(self.matrix_lst[2]) == 3:
            for i in self.matrix_lst:
                for j in i:
                    if type(j) is int:
                        str1 += f'{j:>4}'
                    else:
                        raise TypeError('неверный тип данных')
        else:
            raise ValueError("Incorrect data for Matrix initialization: not equal lenght of lists")
        str2 = str1[0:12] + '\n' + str1[12:24] + '\n' + str1[24:36]
        return str2

    def __add__(self, other):
        str3 = []
        if len(other.matrix_lst) == 3 and len(other.matrix_lst[0]) == 3 and len(other.matrix_lst[1]) == 3 \
                and len(other.matrix_lst[2]) == 3:
            for n in range(len(self.matrix_lst)):
                for m in range(len(self.matrix_lst[n])):
                    sum1 = self.matrix_lst[n][m] + other.matrix_lst[n][m]
                    str3.append(sum1)
        else:
            raise ValueError("Incorrect dimensions for add method")
        str4 = [list(str3[0:3]), list(str3[3:6]), list(str3[6:10])]
        return Matrix(str4)


m1 = Matrix([[11, 2, 3], [4, 5, 6], [117, 8, 9]])
print(m1)
m2 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
print(m2)
m4 = m1 + m2
print(m4)
m3 = Matrix([[1, 1], [1, 1], [1, 1]])
m6 = Matrix([[1, 1, 1, 1], [1, 1, 1], [1, 1, 1]])
