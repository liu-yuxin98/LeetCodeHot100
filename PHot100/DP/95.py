# -*- coding: utf-8 -*-
"""
Created on Sun May 16 11:08:57 2021

@author: Lenovo
"""


def generateTrees(n):
    """
    :type n: int
    :rtype: List[TreeNode]
    """
    def combinetwotree(mid, t1, t2):
        length1 = len(t1)
        length2 = len(t2)
        max_len = max(len(t1), len(t2))

        i = 0
        complete_len = 0
        while True:
            complete_len += 2**i
            if complete_len >= max_len:
                break
            i += 1
        max_depth = i
        res = [mid] + [t1[0]] + [t2[0]]
        i = 0
        while True:
            i += 1
            first = 2**i-1
            if i > max_depth:
                break

            temp1 = []
            for j in range(first, 2**(i+1)-1):
                if j < length1:
                    temp1.append(t1[j])
                else:
                    temp1.append(None)
            f1 = False

            for num in temp1:
                if num:
                    f1 = True
                    break
            if f1 is True:
                res.extend(temp1)
            else:
                pass

            temp2 = []
            for j in range(first, 2**(i+1)-1):
                if j < length2:
                    temp2.append(t2[j])
                else:
                    temp2.append(None)

            f2 = False
            for num in temp2:
                if num:
                    f2 = True
                    break
            if f2:
                res.extend(temp2)
            else:
                pass

        i = len(res)-1
        while True:
            if res[i] is None:
                res.pop()
            else:
                break
            i -= 1
            if res[i] is not None:
                break
        return res
    g = [[] for i in range(n+1)]
    g[0] = [[None]]
    g[1] = [[1]]
    f = [[[] for i in range(n+1)] for j in range(n+1)]
    for j in range(2, n+1):
        for i in range(1, j+1):
            # get f[i][j]
            left = g[i-1]
            right = [[num+i if num else num for num in trees] for trees in g[j-i]]
            for p in range(len(left)):
                for q in range(len(right)):
                    newtree = combinetwotree(i, left[p], right[q])
                    f[i][j].append(newtree)
            g[j].extend(f[i][j])

    return g[n]


def combinetwotree(mid, t1, t2):
    length1 = len(t1)
    length2 = len(t2)
    max_len = max(len(t1), len(t2))

    i = 0
    complete_len = 0
    while True:
        complete_len += 2**i
        if complete_len >= max_len:
            break
        i += 1
    max_depth = i
    res = [mid] + [t1[0]] + [t2[0]]
    i = 0
    while True:
        i += 1
        first = 2**i-1
        if i > max_depth:
            break

        temp1 = []
        for j in range(first, 2**(i+1)-1):
            if j < length1:
                temp1.append(t1[j])
            else:
                temp1.append(None)
        f1 = False

        for num in temp1:
            if num:
                f1 = True
                break
        if f1 is True:
            res.extend(temp1)
        else:
            pass

        temp2 = []
        for j in range(first, 2**(i+1)-1):
            if j < length2:
                temp2.append(t2[j])
            else:
                temp2.append(None)

        f2 = False
        for num in temp2:
            if num:
                f2 = True
                break
        if f2:
            res.extend(temp2)
        else:
            pass

    i = len(res)-1
    while True:
        if res[i] is None:
            res.pop()
        else:
            break
        i -= 1
        if res[i] is not None:
            break
    return res


mid = 1
t1 = [None]
t2 = [2, None, 3]

print(generateTrees(3))
