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


# def spiralOrder(matrix):
#     # set passed number to 0
#     # turn at the boundary
#     m = len(matrix)
#     n = len(matrix[0])
#     output = []
#     move_direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
#     i = 0
#     j = 0
#     direct = 0

#     while True:
#         # out of the matrix
#         if i < 0 or i >= m or j < 0 or j >= n:
#             # to the end?
#             if len(output) == m*n:
#                 break
#             # step back
#             i -= move_direction[direct % 4][0]
#             j -= move_direction[direct % 4][1]
#             # switch direction
#             direct += 1
#             # go one step toward new direction
#             i += move_direction[direct % 4][0]
#             j += move_direction[direct % 4][1]
#         # meet 0 which means need to turn direction
#         elif matrix[i][j] == 0:
#             # to the end?
#             if len(output) == m*n:
#                 break
#             # step back
#             i -= move_direction[direct % 4][0]
#             j -= move_direction[direct % 4][1]
#             # switch direction
#             direct += 1
#             # one step toward new direction
#             i += move_direction[direct % 4][0]
#             j += move_direction[direct % 4][1]
#         else:
#             output.append(matrix[i][j])
#             matrix[i][j] = 0
#             i += move_direction[direct % 4][0]
#             j += move_direction[direct % 4][1]

#     return output

def spiralOrder(matrix):
    i = 0
    j = 0
    m = len(matrix)
    n = len(matrix[0])
    index = 0
    directs = [[0,1],[1,0],[0,-1],[-1,0]]
    res = []
    while True:
        if len(res) == m*n:
            break
        print(i,j)
        res.append(matrix[i][j])
        matrix[i][j] = False
        i += directs[index%4][0]
        j += directs[index%4][1]
        # boundary
        if j == n:
            j -= 1
            i += 1
            index += 1         
        elif i == m:
            i -= 1
            j -= 1
            index += 1
        elif j == -1:
            j += 1
            i -= 1
            index += 1
        # turnning point
        elif matrix[i][j] == False:
            # one step back
            i -= directs[index%4][0]
            j -= directs[index%4][1]
            index += 1
            i += directs[index%4][0]
            j += directs[index%4][1]            
    return res


# more beautiful way
def spiralOrder(matrix):
    # add a boundary to matrix
    for row in matrix:
        row.insert(0, False)
        row.append(False)
    matrix.insert(0,[False]*len(matrix[0]))
    matrix.append([False]*len(matrix[0]))
    i = 1
    j = 1
    index = 0
    directs = [[0,1],[1,0],[0,-1],[-1,0]]
    res = []
    while True:
        if len(res) == (len(matrix)-2)*(len(matrix[0])-2):
            break
        print(index, i,j)
        res.append(matrix[i][j])
        matrix[i][j] = False
        # move forward
        i += directs[index%4][0]
        j += directs[index%4][1]
        # turnning point
        if matrix[i][j] == False:
            # one step back
            i -= directs[index%4][0]
            j -= directs[index%4][1]
            # change direction
            index += 1
            # one step forawrd
            i += directs[index%4][0]
            j += directs[index%4][1]  

    return res
    
matrix = [[1,2,3],[4,5,6],[7,8,9]]

output = spiralOrder(matrix)


