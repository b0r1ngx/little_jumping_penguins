import numpy as np
from sys import stdin
import copy


class MatrixError(BaseException):
    def __init__(self, matrix, other):
        self.matrix1 = matrix
        self.matrix2 = other


class Matrix:
    def __init__(self, matr):
        self.matr = copy.deepcopy(matr)

    def __add__(self, other):
        if np.array(self.matr).shape == np.array(other.matr).shape:
            a = np.array(self.matr) + np.array(other.matr)
            return Matrix(list(map(list, a)))
        else:
            raise MatrixError(self, other)

    def transpose(self):
        tmatrix = list(zip(*self.m1))
        self.m1 = tmatrix
        return Matrix(tmatrix)

    def transposed(self):
        tmatrix = list(zip(*self.m1))
        return Matrix(tmatrix)


exec(stdin.read())
