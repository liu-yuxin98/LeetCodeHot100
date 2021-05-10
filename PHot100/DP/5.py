# -*- coding: utf-8 -*-
"""
Created on Mon May 10 08:53:50 2021

@author: yuxin
"""


def longestPalindrome_1(s):
    ''' first solution to solve longest palindrom problem using center extension
    '''
    # center menthod
    def helper_method(s, left, right):
        if right - left == 2:
            subs = s[left+1]
        else:
            subs = s[left]
        # assume that s[left:right+1] is palindrome.
        while left >= 0 and right <= len(s)-1:
            if s[left] == s[right]:
                subs = s[left:right+1]
                left -= 1
                right += 1
            else:
                break
        return subs
    subs = ''
    for i in range(0, len(s)):
        # center has one letter
        k1 = helper_method(s, i-1, i+1)
        # center has two letters
        k2 = helper_method(s, i, i+1)
        if len(k1) >= len(k2) and len(k1) > len(subs):
            subs = k1
        elif len(k2) > len(k1) and len(k2) > len(subs):
            subs = k2
    return subs


def longestPalindrome_2(s):
    ''' second solution to solve longest palindrom problem using dp
    '''
    n = len(s)
    dp = [[[False] for i in range(n)] for j in range(n)]
    subs = s[0]  # sub string
    i = n-1
    while True:
        if i < 0:
            break
        j = i
        dp[i][j] = True
        while True:
            j += 1
            if j > n-1:
                break
            dp[i][j] = ((dp[i+1][j-1] or i == j-1) and s[i] == s[j])
            # check if dp[i][j] is true and its corresponding substring
            if dp[i][j] and j+1-i >= len(subs):
                subs = s[i:j+1]
        i -= 1
    return subs


def longestPalindrom_3(s):
    # Manacher algorithm
    def pre_process(s):
        # pre process of s
        s = list(s)
        return '|'+'|'.join(s)+'|'

    return pre_process(s)

s = 'abba'
print(longestPalindrom_3(s))
