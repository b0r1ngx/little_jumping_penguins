from copy import deepcopy
from sys import stdin


class MatrixError(BaseException):
    def __init__(self, m1, m2):
        self.matrix1 = m1
        self.matrix2 = m2


class Matrix:
    def __init__(self, m):
        self.m = copy.deepcopy(m)

    def __str__(self):
        str_m = '\n'.join(['\t'.join([str(j) for j in i]) for i in self.m])
        return str_m

    def size(self):
        return len(self.m), len(self.m[0])

    def __add__(self, other):
        if other != self:
            RuntimeError()
        else:
            res = Matrix
            res.m = []
            temp = []
            for i in range(len(self.m)):
                for j in range(len(self.m[0])):
                    x = self.m[i][j] + other.m[i][j]
                    temp.append(x)
                    if len(temp) == len(self.m):
                        res.m.append(temp)
                        temp = []
            return Matrix(res.m)

    def __mul__(self, n):
        c = [[n * row for row in column] for column in self.m]
        return Matrix(c)

    __rmul__ = __mul__

    def transpose(self):
        result = Matrix
        result.m = []
        for i in range(len(self.m[0])):
            temp = []
            for j in range(len(self.m)):
                x = self.m[j][i]
                temp.append(x)
            result.m.append(temp)
        self.m = result.m
        return Matrix(self.m)

    @staticmethod
    def transposed(object):
        result = []
        for i in range(len(object.m[0])):
            temp = []
            for j in range(len(object.m)):
                x = object.m[j][i]
                temp.append(x)
            result.append(temp)
        return Matrix(result)


exec(stdin.read())
