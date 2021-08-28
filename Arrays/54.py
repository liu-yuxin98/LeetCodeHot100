# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 15:11:15 2021

@author: Lenovo
"""


# def spiralOrder(matrix):
#     """
#     :type matrix: List[List[int]]
#     :rtype: List[int]
#     """
#     n = len(matrix)*len(matrix[0])
#     output = []
#     matrix = [[-101] + row + [-101] for row in matrix]
#     matrix.insert(0, [-101]*len(matrix[0]))
#     matrix.append([-101]*len(matrix[0]))

#     direction = ['right', 'down', 'left', 'up']
#     direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
#     change_times = 0

#     i = 1
#     j = 1
#     value = matrix[i][j]
#     matrix[i][j] = -101
#     output.append(value)
#     while True:
#         # to the last
#         if len(output) >= n:
#             break
#         while True:
#             i += direction[change_times%4][0]
#             j += direction[change_times%4][1]
#             if matrix[i][j] == -101:
#                 i -= direction[change_times%4][0]
#                 j -= direction[change_times%4][1]
#                 change_times += 1
#                 break
#             value = matrix[i][j]
#             matrix[i][j] = -101
#             output.append(value)
#     return output


def spiralOrder(matrix):
    # set passed number to 0
    # turn at the boundary
    m = len(matrix)
    n = len(matrix[0])
    output = []
    move_direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    i = 0
    j = 0
    direct = 0

    while True:
        # out of the matrix
        if i < 0 or i >= m or j < 0 or j >= n:
            # to the end?
            if len(output) == m*n:
                break
            # step back
            i -= move_direction[direct % 4][0]
            j -= move_direction[direct % 4][1]
            # switch direction
            direct += 1
            # go one step toward new direction
            i += move_direction[direct % 4][0]
            j += move_direction[direct % 4][1]
        # meet 0 which means need to turn direction
        elif matrix[i][j] == 0:
            # to the end?
            if len(output) == m*n:
                break
            # step back
            i -= move_direction[direct % 4][0]
            j -= move_direction[direct % 4][1]
            # switch direction
            direct += 1
            # one step toward new direction
            i += move_direction[direct % 4][0]
            j += move_direction[direct % 4][1]
        else:
            output.append(matrix[i][j])
            matrix[i][j] = 0
            i += move_direction[direct % 4][0]
            j += move_direction[direct % 4][1]

    return output


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
output = spiralOrder(matrix)


