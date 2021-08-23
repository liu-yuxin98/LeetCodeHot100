# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 20:06:50 2021

@author: Lenovo
"""

def numBusesToDestination( routes, source, target):
    """
    :type routes: List[List[int]]
    :type source: int
    :type target: int
    :rtype: int
    """
    return


class UnionFind():

    def __init__(self, union):
        self.union = union

    def union(self, v1, v2):
        import math
        i = self.union.index(v1)
        j = self.union.index(v2)
        root1 = self.find_root[i]
        root2 = self.find_root[j]
        if math.fabs(self.union[root1]) > math.fabs(self.union[root2]):
            self.union[root1] -= self.union[root2]
            self.union[root2] = root1

        else:
            self.union[root2] -= self.union[root1]
            self.union[root1] = root2

    def find_root(self, i):
        if self.union[i] < 0:
            return i
        self.find_root(self.union[i])

    def print_out(self):
        print(self.union)


union = [7, 12, 4, 5]
uf = UnionFind(union)
uf.print_out()

uf.print_out()
