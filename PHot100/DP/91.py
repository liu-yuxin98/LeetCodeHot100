# -*- coding: utf-8 -*-
"""
Created on Sun May 16 16:37:44 2021

@author: Lenovo
"""

def numDecodings(s):
    # very disgusting. I can't fix it out
    """
    :type s: str
    :rtype: int
    """
    s = [int(num) for num in s]
    if s[0] == 0:
        return 0
    else:
        f = [0 for i in range(len(s))]
        f[0] = 1
        for i in range(1, len(s)):
            if 0 < (s[i-1]*10+s[i]) <= 26 and s[i] > 0:
                f[i] = f[i-1] +1
            else:
                f[i] = f[i-1]
        return f[-1]

s = "10"

print(numDecodings(s))