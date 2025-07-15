#задание 13
import random

def CreateMarpix( x, y, startV, endV):
    return [[random.randint( startV, endV) for i in range(x)] for i in range(y)]

def ZeroMatrix( x, y):
    return [[0 for i in range(x)] for i in range(y)]

def printMatrix(m):
    for i in m:
        print(*i)

def ErrorMatrixSize():
    print("размерность матриц не совпадает")


def MatrixAddition(m1, m2):
    if(len(m1) != len(m2)):
        ErrorMatrixSize()
        return False
    if(len(m1[0]) != len(m2[0])):
        ErrorMatrixSize()
        return False
    y= len(m1)
    x= len(m1[0])
    res = ZeroMatrix(x, y)
    for i in range(y):
        for j in range(x):
            res[i][j] = m1[i][j]+m2[i][j]
    return res



x,y = map(int, input("Введите размерность матриц через пробел : ").split())
st = int(input("Введите начало случейных значений : "))
en = int(input("Введите конец случайных значение : "))

m1 = CreateMarpix( x, y, st, en)
printMatrix(m1)
print()
m2 = CreateMarpix( x, y, st, en) 
printMatrix(m2)

m3 = MatrixAddition(m1, m2)

print("Сложенная матрица")
printMatrix(m3)
