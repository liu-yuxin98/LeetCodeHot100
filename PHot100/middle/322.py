# -*- coding: utf-8 -*-
"""
Created on Fri May  7 21:29:14 2021

@author: Yuxin
"""

def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    import sys
    f = [sys.maxsize]*(amount+1)
    f[0] = 0
    for i in range(1, amount+1):
        res = []
        for coin in coins:
            if i - coin < 0:
                res.append(sys.maxsize)
            else:
                res.append(f[i-coin])
        f[i] = min(min(res)+1, sys.maxsize)

    for i in range(1, amount+1):
        if f[i] == sys.maxsize:
            f[i] = -1
    return f[amount]

print(coinChange([2], 3))
