# -*- coding: utf-8 -*-
"""
Created on Sun March 26 05:36:11 2023
@author: Lenovo
"""
import numpy as np
import random
import time
import copy

# ------------------------ select sort ----------------------------------------


def select_sort(nums):
    for i in range(len(nums)-1):
        min_index = i
        for j in range(i, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]


# ------------------------ bubble sort ----------------------------------------
def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]


# ------------------------ insert sort ----------------------------------------
def insert_sort(nums):
    for i in range(1, len(nums)):
        j = i-1
        key = nums[i]
        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key


# ------------------------ shell sort -----------------------------------------
def shell_sort(nums):
    step = int(len(nums)/2)
    while step > 0:
        for i in range(step, len(nums)):
            # insert nums[i] to sorted one
            key = nums[i]
            j = i
            while j >= step and nums[j-step] > key:
                nums[j] = nums[j-step]
                j -= step
            nums[j] = key
        step = int(step/2)


# ------------------------ merge sort -----------------------------------------
def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums)//2
    left = merge_sort(nums[0:mid])
    right = merge_sort(nums[mid::])
    sorted_nums = merge_two_list(left, right)
    return sorted_nums


def merge_two_list(nums1, nums2):
    if nums1 == [] or nums2 == []:
        return nums1 + nums2
    else:
        res = []
        i = 0
        j = 0
        while True:
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
                if i >= len(nums1):
                    res.extend(nums2[j::])
                    break
            else:
                res.append(nums2[j])
                j += 1
                if j >= len(nums2):
                    res.extend(nums1[i::])
                    break
    return res


# ------------------------ qucik sort -----------------------------------------
def quickSort(nums):
    quick_sort_Helper(nums, 0, len(nums)-1)

# Function to find the partition position


def partition(array, low, high):
    pivot = array[low]
    while(low < high):
        while(low < high and array[high] >= pivot):
            high -= 1
        # find a array[right] < pivot
        array[low] = array[high]
        while(low < high and array[low] <= pivot):
            low += 1
        array[high] = array[low]
    array[low] = pivot
    return low

# Function to perform quicksort


def quick_sort_Helper(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        # Recursive call on the left of pivot
        quick_sort_Helper(array, low, pi - 1)
        # Recursive call on the right of pivot
        quick_sort_Helper(array, pi + 1, high)


# ------------------------ heap sort ------------------------------------------
def heapify(tree, n, i):
    if i >= n:
        return
    c1 = 2*i+1
    c2 = 2*i+2
    max_index = i
    if c1 < n and tree[c1] > tree[i]:
        max_index = c1
    if c2 < n and tree[c2] > tree[max_index]:
        max_index = c2
    if max_index != i:
        tree[max_index], tree[i] = tree[i], tree[max_index]
        heapify(tree, n, max_index)


def build_heap(tree, n):
    last_node = n-1
    last_parent = (last_node-1)//2
    for i in range(last_parent, -1, -1):
        heapify(tree, n, i)


def heap_sort(nums):
    end = len(nums)
    build_heap(nums, end)
    i = end-1
    while True:
        if i < 0:
            break
        nums[0], nums[i] = nums[i], nums[0]
        heapify(nums, i, 0)
        i -= 1


t1 = time.time()
for i in range(100):
    nums = list(np.random.randint(100, size=random.randint(0, 10)))
    nums1 = copy.deepcopy(nums)
    nums1.sort()
    quickSort(nums)
    if not nums1 == nums:
        print('FFFFFFalse')
        print(nums)
        break
t2 = time.time()
# print(t2-t1)
# import random

#     temp = sorted(temp)
#     print(res == temp)
