#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    # Create a new matrix to store the squared values
    result_matrix = []

    # Iterate through the rows of the input matrix
    for row in matrix:
        # Create a new row with squared values using a list comprehension
        squared_row = [x**2 for x in row]
        # Append the squared row to the result matrix
        result_matrix.append(squared_row)

    return result_matrix


if __name__ == "__main__":
    # Example usage:
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    result = square_matrix_simple(matrix)
    print(result)