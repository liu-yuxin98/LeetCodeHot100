# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 09:51:27 2021

@author: Lenovo
"""


# def reverseParentheses(s):
#         i = 0
#         stack = []
#         while True:
#             if i > len(s)-1:
#                 break
#             if s[i] != ')':
#                 stack.append(s[i])
#             else:
#                 temp = []
#                 while True:
#                     if stack[-1] == '(':
#                         stack.pop()
#                         break
#                     else:
#                         temp.append(stack.pop())
#                 stack.extend(temp)
#             i += 1
#         return ''.join(stack)


# def reverseParentheses(s):
#     i = 0
#     stack = []
#     while True:
#         if i >= len(s):
#             break
#         if s[i] != ')':
#             stack.append(s[i])
#         else:
#             temp = []
#             while stack:
#                 if stack[-1] == '(':
#                     stack.pop()
#                     break
#                 temp.append(stack.pop())
#             stack.extend(temp)
#         i += 1

#     return ''.join(stack)

def reverseParentheses(s):
    stack = []
    i = 0
    while True:
        if i >= len(s):
            break
        elif s[i] ==')':
            temp = []
            while True:
                if stack == []:
                    break
                c = stack.pop()
                if c == '(':
                    break
                else:
                    temp.append(c)
            stack.extend(temp)    
        else:
            stack.append(s[i])
        i += 1       
    return ''.join(stack)

s = "(abcd)"
# s = '(u(love)i)'
# s = "(ed(et(oc))el)"
res = reverseParentheses(s)