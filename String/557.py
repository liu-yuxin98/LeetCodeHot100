# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 11:41:34 2021

@author: Lenovo
"""
def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    s = s.split(' ')
    s = [c[::-1] for c in s]
    s = ' '.join(s)
    return s

s = "Let's take LeetCode contest"

print(reverseWords(s))
