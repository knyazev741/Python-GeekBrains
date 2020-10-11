matrix1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

matrix2 = [
    [17, 18, 19, 20],
    [21, 22, 23, 24],
    [25, 26, 27, 28],
    [29, 30, 31, 32]
]


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return f"{self.matrix[0]}\n{self.matrix[1]}\n{self.matrix[2]}\n{self.matrix[3]}"

    def __add__(self, other):
        new_matrix = [
            [self.matrix[0][0] + other.matrix[0][0], self.matrix[0][1] + other.matrix[0][1],
             self.matrix[0][2] + other.matrix[0][2], self.matrix[0][3] + other.matrix[0][3]],
            [self.matrix[1][0] + other.matrix[1][0], self.matrix[1][1] + other.matrix[1][1],
             self.matrix[1][2] + other.matrix[1][2], self.matrix[1][3] + other.matrix[1][3]],
            [self.matrix[2][0] + other.matrix[2][0], self.matrix[2][1] + other.matrix[2][1],
             self.matrix[2][2] + other.matrix[2][2], self.matrix[2][3] + other.matrix[2][3]],
            [self.matrix[3][0] + other.matrix[3][0], self.matrix[3][1] + other.matrix[3][1],
             self.matrix[3][2] + other.matrix[3][2], self.matrix[3][3] + other.matrix[3][3]]
        ]

        return Matrix(new_matrix)


m1 = Matrix(matrix1)
m2 = Matrix(matrix2)
m3 = m1 + m2

print(m3)
