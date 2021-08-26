# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 14:58:07 2021

@author: Lenovo
"""


def largestRectangleArea(heights):
    # for each pillar heights[i], we will find its left and right bound
    left_bound = find_bound(heights, True)
    right_bound = find_bound(heights, False)
    cur_max = 0
    for i in range(len(heights)):
        left_pillar = left_bound[i]
        right_pillar = right_bound[i]
        width = right_pillar - left_pillar-1
        area = width * heights[i]
        cur_max = max(cur_max, area)
    return cur_max


def find_bound(heights, isleft):
    # for every pillar heights[i] we want to find the nearest pillar heights[j]
    # where j<i and heights[j] < heights[i]
    left_bound = [0]*len(heights)
    left_bound[0] = -1
    if not isleft:
        heights = heights[::-1]
    stack = [[heights[0], 0]]
    for i in range(len(heights)):

        h = heights[i]
        if h > stack[-1][0]:
            left_bound[i] = stack[-1][1]
            stack.append([h, i])
        else:
            while True:
                stack.pop()
                if stack == []:
                    left_bound[i] = -1
                    stack.append([h, i])
                    break
                if h > stack[-1][0]:
                    left_bound[i] = stack[-1][1]
                    stack.append([h, i])
                    break
    if not isleft:
        left_bound = [len(heights)-pos-1 if pos != -1 else len(heights) for pos in left_bound]
        left_bound = left_bound[::-1]
    return left_bound


# def largestRectangleArea(heights):
#     # 88/96 pass
#     """
#     :type heights: List[int]
#     :rtype: int
#     """
#     possible_rectangle = {}
#     trace_list = []
#     cur_max = 0
#     for i in range(len(heights)):
#         height = heights[i]
#         for h in range(1, height+1):
#             if h not in trace_list:
#                 trace_list.append(h)
#                 possible_rectangle[h] = [i, i]
#         j = 0
#         while j < len(trace_list):
#             key = trace_list[j]
#             if key <= height:
#                 possible_rectangle[key][1] = i
#             else:
#                 area = key*(possible_rectangle[key][1]-possible_rectangle[key][0]+1)
#                 possible_rectangle[key] = [i, i-1]
#                 cur_max = max(cur_max, area)
#                 trace_list.pop(j)
#                 j -= 1
#             j += 1
#     for key in possible_rectangle:
#         area = key*(possible_rectangle[key][1]-possible_rectangle[key][0]+1)
#         cur_max = max(cur_max, area)
#     return cur_max

heights = [6, 7, 5, 2, 4, 5, 9, 3]

max_area = largestRectangleArea(heights)
