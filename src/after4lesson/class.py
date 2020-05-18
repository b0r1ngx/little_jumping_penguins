from sys import stdin
import copy


class Matrix(list):
    def __init__(self, m):
        self.m = copy.deepcopy(m)

    def __str__(self):
        str_m = '\n'.join(['\t'.join([str(j) for j in i]) for i in self.m])
        return str_m

    def __add__(self, other):
        if other == self:
            print()
        else:
            RuntimeError('Error')

    def __mul__(self, n):
        print()

    __rmul__ = __mul__

    def size(self):
        return len(self.m), len(self.m[0])


exec(stdin.read())
