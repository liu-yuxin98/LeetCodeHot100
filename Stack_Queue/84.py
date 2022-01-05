# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 16:07:24 2021

@author: Lenovo
"""

# exceeds time limit
def largestRectangleArea(heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_area = heights[0]
        for i in range(len(heights)):
            left_area = 0
            right_area = 0
            for right in range(i,len(heights)):
                if heights[right] < heights[i]:
                    right_area = max(right_area, heights[i]*(right-i-1))
                    break
            else:
                right_area = max(right_area, heights[i]*(len(heights)-i-1))
            for left in range(i,-1,-1):
                if heights[left] < heights[i]:
                    left_area = max(left_area,heights[i]*(i-left-1))
                    break
            else:
                left_area = heights[i]*i
            area = heights[i] + left_area + right_area
            max_area = max(max_area,area)
        return max_area
            
            
# pass using list
def largestRectangleArea(heights):  
    # RECORDS the most right bar on bar i's left side whose height is smaller than bar i
    less_left_bar = [-1]*len(heights)
    # RECORDS the most left bar on bar i's right side whose height is smaller than bar i
    less_right_bar = [len(heights)]* len(heights)
    
    # key problem is to calculate less_left_bar and less_right_bar fast
    # calculate less_left_bar
    for i in range(1, len(less_left_bar)):
        j = i-1
        while True:
            if j < 0 or heights[j] < heights[i]:
                break
            j = less_left_bar[j]  
        less_left_bar[i] = j
    # calculate less_right_bar
    for i in range(len(less_left_bar)-2,-1,-1):
        j = i+1
        while True:
            if j >=len(heights) or heights[j] < heights[i]:
                break
            j = less_right_bar[j]  
        less_right_bar[i] = j            
    
    max_area = 0
    for i in range(len(heights)):
        max_area = max(max_area, heights[i]*(less_right_bar[i]-less_left_bar[i]-1))
    return max_area
 

# 单调栈
def largestRectangleArea(heights):
        left_less_stack = []
        right_less_stack = []
        left_boundary = []
        right_boundary = []
        size = len(heights)
        # from left to right
        for i in range(size):
            # find left boundary
            while True:
                if left_less_stack == []:
                    left = -1
                    left_less_stack.append(i)
                    break
                if heights[i] > heights[left_less_stack[-1]]:
                    left = left_less_stack[-1]
                    left_less_stack.append(i)
                    break
                elif heights[i] <= heights[left_less_stack[-1]]:
                    left_less_stack.pop()
            left_boundary.append(left)
            # from right to left
        right_boundary = [1]*size
        for i in range(size-1,-1,-1):
            # find right boundary
            while True:
                if right_less_stack == []:
                    right = size
                    right_less_stack.append(i)
                    break
                if heights[i] > heights[right_less_stack[-1]]:
                    right = right_less_stack[-1]
                    right_less_stack.append(i)
                    break
                else:
                    right_less_stack.pop()
            right_boundary[i] = right
                
        max_area = 0
        for i in range(size):
            max_area = max(max_area, heights[i]*(right_boundary[i]-left_boundary[i]-1))         
        print(left_boundary)
        print(right_boundary)            
        return max_area                        



def single_stack(heights):
    stack = []
    for i in range(len(heights)):
        if stack == []:
            stack.append(heights[i])
            print('push ',heights[i])

        while True:
            if stack == []:
               stack.append(heights[i])
               print('push ',heights[i])
               break
            if heights[i] > stack[-1]:
                value = stack.pop()
                print('pop ',value)
            elif heights[i] == stack[-1]:
                break
            else:
                stack.append(heights[i])
                print('push ',heights[i])
                break
        print(stack)
        print('-------------')


#单调栈            
def largestRectangleArea( heights:list[int]) -> int:
        size = len(heights)
        res = 0
        stack = []
    
        for i in range(size):
            while len(stack) > 0 and heights[i] < heights[stack[-1]]:
                cur_height = heights[stack.pop()]
    
                while len(stack) > 0 and cur_height == heights[stack[-1]]:
                    stack.pop()
    
                if len(stack) > 0:
                    cur_width = i - stack[-1] - 1
                else:
                    cur_width = i
    
                res = max(res, cur_height * cur_width)
            stack.append(i)

        while len(stack) > 0:
            cur_height = heights[stack.pop()]
            while len(stack) > 0 and cur_height == heights[stack[-1]]:
                stack.pop()
    
            if len(stack) > 0:
                cur_width = size - stack[-1] - 1
            else:
                cur_width = size
            res = max(res, cur_height * cur_width)
    
        return res

 
heights = [2,1,5,6,2,3]  
# single_stack(heights)
output = largestRectangleArea(heights)