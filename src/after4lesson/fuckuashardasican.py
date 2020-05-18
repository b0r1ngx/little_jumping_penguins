from sys import stdin
import copy


class Matrix(list):
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


exec(stdin.read())
