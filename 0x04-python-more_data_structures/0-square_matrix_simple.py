#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    power = [[list(map(lambda x:x**2,row))]for row in matrix]
    return power


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result = square_matrix_simple(matrix)
print(result)
print(matrix)