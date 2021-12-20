# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 23:39:34 2021

@author: Lenovo
"""


# def minWindow(s, t):
#     """
#     :type s: str
#     :type t: str
#     :rtype: str
#     """

#     if len(t) > len(s):
#         return ""
#     need = {}
#     for c in t:
#         if c in need:
#             need[c] += 1
#         else:
#             need[c] = 1
#     i = 0
#     j = 0
#     min_length = len(s)
#     contained_key = 0
#     best_solution = ""
#     while True:
#         if j >= len(s):
#             break

#         if s[j] in need:
#             need[s[j]] -= 1
#             if need[s[j]] >= 0:
#                 contained_key += 1
#         # print(i, j, best_solution, contained_key)
#         if contained_key == len(t):
#             # add i
#             while True:
#                 if i > j:
#                     break
#                 if s[i] in need:
#                     need[s[i]] += 1
#                     # s[i] is must?
#                     if need[s[i]] > 0:
#                         contained_key -= 1
#                     # can not fulfill request
#                     if need[s[i]] >= 1:
#                         if j-i+1 <= min_length:
#                             min_length = j-i+1
#                             best_solution = s[i:j+1]
#                             if min_length == len(t):
#                                 return best_solution
#                         i += 1
#                         break
#                 i += 1
#         j += 1
#     return best_solution


# ----------------------字节面试遇到的---------------
# def minWindow(s, t):
#     i = 0
#     j = 0
#     min_length = len(s)
#     need_c = dict()
#     solution = []
#     needs = len(t)
#     for c in t:
#         if c not in need_c:
#             need_c[c] = 1
#         else:
#             need_c[c] += 1

#     while True:
#         if j >= len(s):
#             break
#         if s[j] in t:
#             need_c[s[j]] -= 1
#             if need_c[s[j]] >= 0:
#                 needs -= 1
#             if needs == 0:
#                 while True:
#                     if s[i] in t:
#                         if need_c[s[i]] < 0:
#                             need_c[s[i]] += 1
#                             i += 1
#                         else:
#                             break
#                     else:
#                         i += 1
#                 if j-i+1 <= min_length:
#                     min_length = j-i+1
#                     solution = [i, j]
#         else:
#             pass
#         j += 1
#     if solution != []:
#         res = s[int(solution[0]): int(solution[1])+1]
#         return res
#     else:
#         return ""
def minWindow(s, t):
    if len(t)>len(s):
        return ''
    need_dict = {}
    for key in t:
        need_dict[key] = need_dict.get(key,0)+1
    start = 0
    end = 0
    find =  False
    res = s[::]
    while True:
        if end >= len(s) or start >= len(s):
            break
        if s[start] in t:
            need_dict[s[start]] -= 1
            # decide if contains all charter in t
            for key in need_dict:
                if need_dict[key] > 0:
                    break
            else:
                find = True            
            if find:
                res = s[start:end+1]
            end = start + 1
            while True:
                # move end forward
                if end >= len(s):
                    break
                if s[end] in t:
                    need_dict[s[end]] -= 1
                    # decide if contains all charter in t
                    for key in need_dict:
                        if need_dict[key] > 0:
                            break
                    else:
                        find = True
                    if find:
                        # move start forward
                        while True:
                            if s[start] in t:
                                if need_dict[s[start]] == 0:
                                    if (end+1-start) <= len(res):
                                        res = s[start:end+1]
                                    break
                                else:
                                    need_dict[s[start]] += 1
                                    start += 1
                            else:
                                start += 1
                end += 1
        start += 1
        end = max(start,end)
    if find:
        return res
    return ''

    
output = minWindow('ab', 'b')


# import unittest

# class TestStringMethods(unittest.TestCase):
    
#     def test_minWindow(self):
#         self.assertEqual(minWindow('A', 'A'), 'A')
#         self.assertEqual(minWindow('Ab', 'b'), 'b')
#         self.assertEqual(minWindow("ABCEFG", 'BCG'), 'BCEFG')
#         self.assertEqual(minWindow('ADOBECODEBANC', 'ABC'), 'BANC')
#         self.assertEqual(minWindow('a', 'aa'), '')

# if __name__ == '__main__':
#     unittest.main()


