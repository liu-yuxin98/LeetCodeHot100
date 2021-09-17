# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 01:22:15 2021

@author: Lenovo
"""


def longestValidParentheses(s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) <= 1:
        return 0
    # dp[i] 表示以s[i]结尾的最长的有效括号的长度
    dp = [0] * len(s)
    dp[0] = 0
    for i in range(1, len(s)):
        if s[i] == ')':
            pre_bound = (i-1) - dp[i-1]
            if pre_bound >= 0 and s[pre_bound] == '(':
                # 判断 dp[pre_bound-1]
                if pre_bound >= 1:
                    dp[i] = dp[i-1] + 2 + dp[pre_bound-1]
                else:
                     dp[i] = dp[i-1] + 2

    return max(dp)


s = ")(()()())"
m = longestValidParentheses(s)
