#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda submat:list(map(lambda x:x**2,submat)), matrix))


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result = square_matrix_simple(matrix)
print(result)
print(matrix)
