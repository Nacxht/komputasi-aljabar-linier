import math

A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [4, 5, 6, 7]
]

B = [
    [8, 7, 6, 5],
    [4, 3, 2, 1],
    [7, 6, 5, 4]
]

# Ambil satu elemen
def getC(row, col):
    return A[row][col] + B[row][col]

C = getC(2, 2)
# print(C)

# Skalar
A_New = []

for i in range(len(A)):
    A_New.append([])
    
    for j in range(len(A[i])):
        A_New[i].append(A[i][j] * 2)

print(A_New)

# 