#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squar_list = []
    for i in range(len(matrix)):
        squar = []
        for j in range(len(matrix[i])):
            result = matrix[i][j] ** 2
            squar.append(result)
        squar_list.append(squar)
    return (squar_list)
