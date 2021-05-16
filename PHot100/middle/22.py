# -*- coding: utf-8 -*-
"""
Created on Sun May 16 19:35:07 2021

@author: yuxin
"""


def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    f = [[] for i in range(n+1)]
    f[0] = ['']
    f[1] = ['()']
    for i in range(2, n+1):
        for p in range(0, i):
            q = i-p-1
            fp = f[p]
            fq = f[q]
            for itemp in fp:
                for itemq in fq:
                    newitem = '('+itemp+')'+itemq
                    f[i].append(newitem)
    return f[n]

print(generateParenthesis(3))
            
