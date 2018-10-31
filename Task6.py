import numpy as np


# Problem 1
def getdimension(a):
    return a.ndim


# Problem 2
def getdiagonal(a):
    return a.diagonal()


# Problem 3
def cutarray(a, minvalue, maxvalue):
        return np.clip(a, minvalue, maxvalue)


# Problem 4
def getmoments(a):
    return (np.mean(a), np.var(a))


# Problem 5
def getdotproduct(a, b):
    return np.dot(a,b)


# Problem 6
def checkequal(a, b):
    return np.isclose(a,b)


# Problem 7
def comparewithnumber(a, bound):
    return np.less(a, bound)


# Problem 8
def matrixproduct(a, b):
    return np.matmul(a,b)


# Problem 9
def matrixdet(a):
    return np.linalg.det(a)


# Problem 10
def getones(n, k):
    return np.eye(n, k=k)






    












