# -*- coding: utf-8 -*-
"""
Created on Sat May  8 13:52:35 2021

@author: YUXIN
"""

def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    i = 0
    j = 0
    # j  go through t
    while True:
        if i == len(s):
            return True
        # find s[i] in t
        while True:
            # out of boundary
            if j > len(t)-1:
                return False
            # find j
            if s[i] == t[j]:
                if i == len(s)-1:
                    return True
                # move i forward
                i += 1
                break
            j += 1
        j += 1
        if j > len(t)-1:
            return False

    # ps = 0
    # pi = 0
    # s = list(s)
    # t = list(t)
    # if len(s) == 0:
    #     return True
    # if len(s) > len(t):
    #     return False
    # while pi < len(t):
    #     # find pi to make t[pi] = s[ps]
    #     while True:
    #         if t[pi] == s[ps]:
    #             # reach the end of s and find s[-1] in t
    #             if ps == len(s)-1:
    #                 return True
    #             # move pointer ps forward
    #             else:
    #                 ps += 1
    #                 break
    #         # move pointer pi forward
    #         pi += 1
    #         # boundary
    #         if pi >= len(t):
    #             return False
    #     # move pointer pi forward
    #     pi += 1
    # if pi == len(t):
    #     return False


s = "abc"
t = "abdc"
print(isSubsequence(s,t))

