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

def lengthOfLongestSubstring(s):
    start = 0
    end = 0
    output = 0
    pos_dict = {}
    while True:
        if end >= len(s) or start > end:
            break
        if s[end] not in s[start:end]:
            pos_dict[s[end]] = end
        else:
            start = max(pos_dict[s[end]]+1, start)
            pos_dict[s[end]] = end
        output = max(output, end-start+1)
        end += 1
    return output

s = " "
output = lengthOfLongestSubstring(s)

s = ''
print('a' in s)