# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 23:39:34 2021

@author: Lenovo
"""


def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """

    if len(t) > len(s):
        return ""
    need = {}
    for c in t:
        if c in need:
            need[c] += 1
        else:
            need[c] = 1
    i = 0
    j = 0
    min_length = len(s)
    contained_key = 0
    best_solution = ""
    while True:
        if j >= len(s):
            break

        if s[j] in need:
            need[s[j]] -= 1
            if need[s[j]] >= 0:
                contained_key += 1
        # print(i, j, best_solution, contained_key)
        if contained_key == len(t):
            # add i
            while True:
                if i > j:
                    break
                if s[i] in need:
                    need[s[i]] += 1
                    # s[i] is must?
                    if need[s[i]] > 0:
                        contained_key -= 1
                    # can not fulfill request
                    if need[s[i]] >= 1:
                        if j-i+1 <= min_length:
                            min_length = j-i+1
                            best_solution = s[i:j+1]
                            if min_length == len(t):
                                return best_solution
                        i += 1
                        break
                i += 1
        j += 1
    return best_solution

s = "A"
t = "A"
res = minWindow(s, t)


