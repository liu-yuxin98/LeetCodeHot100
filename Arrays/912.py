# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 20:14:19 2021

@author: Lenovo
"""


def sortArray(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    def heapify(i, end, tree):
        if i >= end:
            return
        child1 = 2*i+1
        child2 = 2*i+2
        max_i = i
        if child1 < end and tree[child1] > tree[max_i]:
            max_i = child1
        if child2 < end and tree[child2] > tree[max_i]:
            max_i = child2
        if i != max_i:
            tree[i], tree[max_i] = tree[max_i], tree[i]
            heapify(max_i, end, tree)

    def buildheap(end, tree):
        last_i = end-1
        last_parent = (last_i - 1) // 2
        while last_parent >= 0:
            heapify(last_parent, end, tree)
            last_parent -= 1

    end = len(nums)
    buildheap(end, nums)
    while True:
        if end <= 1:
            break
        heapify(0, end, nums)
        nums[0], nums[end-1] = nums[end-1], nums[0]
        end -= 1




nums = [5, 2, 3, 1]
sortArray(nums)
