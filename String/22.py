# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 22:58:05 2021

@author: Lenovo
"""

def generateParenthesis(n):
    dp = [ [] for i in range(n+1)]
    dp[1] = ['()']
    for i in range(2, n+1):
        all_combine = []
        for j in range(len(dp[i-1])):
            item = dp[i-1][j]
            for k in range(len(item)+1):
                if k == 0:
                    new_item = '()' + item
                else:
                    new_item = item[0:k] + '()' + item[k::]
                if new_item not in all_combine:
                    all_combine.append(new_item)
        dp[i] = all_combine
    return dp[n]

print(generateParenthesis(1))