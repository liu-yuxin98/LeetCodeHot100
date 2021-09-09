# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 11:47:56 2021

@author: Lenovo
"""


def lengthOfLongestSubstring(s):
    posdict = dict()
    i = 0
    j = 0
    max_length = 0

    while True:
        if j >= len(s) or i > j:
            break
        if s[j] not in posdict:
            posdict[s[j]] = j
        else:  # s[j] in posdict
            i = max(posdict[s[j]] + 1, i)
            posdict[s[j]] = j
        max_length = max(max_length, j-i+1)
        j += 1
    return max_length

s = "abba"
output = lengthOfLongestSubstring(s)