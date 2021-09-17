# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 21:57:36 2021

@author: Lenovo
"""


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Linked_List:

    def __init__(self):
        self.root = Node(None)

    def add(self, value):
        p = self.root
        while True:
            if p.next is None:
                p.next = Node(value)
                break
            p = p.next

    def info(self):
        p = self.root
        values = []
        while True:
            if p is None:
                break
            values.append(p.value)
            p = p.next
        print(values)

    def create_linked_list(nums):
        lst = Linked_List()
        if len(nums) == 0:
            lst.root = Node(None)
            return lst
        lst.root = Node(nums[0])
        p = lst.root
        for i in range(1, len(nums)):
            p.next = Node(nums[i])
            p = p.next
        return lst



def reverse_list(root, k):
    p = root
    length = 1
    while p.next is not None:
        p = p.next
        length += 1
    first_seg = length % k
    # go to the first_seg
    start = root
    if first_seg == 0:
        pre = root
    else:
        for i in range(first_seg-1):
            start = start.next
        pre = start
        start = start.next
    # from start, we do reverse with k item as a group

    return 1


def reverse(head):
    pre_head = head
    next_head = head.next
    head.next = None
    print(pre_head.value, head.value, next_head.value)
    while True:
        head = next_head
        if head.next is None:
            head.next = pre_head
            return head
        next_head = head.next
        head.next = pre_head
        pre_head = head
        print(pre_head.value, head.value, next_head.value)


nums =[i for i in range(1,6)]
lst = Linked_List.create_linked_list(nums)
lst.info()
lst.root = reverse(lst.root)
lst.info()
