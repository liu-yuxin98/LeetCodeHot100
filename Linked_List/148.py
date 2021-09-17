# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 10:22:11 2021

@author: Lenovo
"""


class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def info(head):
    p = head
    values = []
    while True:
        if p is None:
            break
        values.append(p.val)
        p = p.next
    print(values)

def sortList( head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head is None:
        return None
    left, pos, right = partition(head)

    if left is None and right is None:
        return pos
    if left is None:
        left_sorted = None
    else:
        left_sorted = sortList(left)
    if right is None:
        right_sorted = None
    else:
        right_sorted = sortList(right)

    temp_left = left_sorted
    if temp_left is None:
        pos.next = right_sorted
        head = pos
    else:
        while True:
            if temp_left.next is None:
                temp_left.next = pos
                pos.next = right_sorted
                head = left_sorted
                break
            temp_left = temp_left.next
    return head


def partition(head):
    pos = head
    val = head.val
    p = head.next
    if p is None:
        return None, head, None
    pre = head
    while True:
        if p is None:
            break
        if p.val < val:
            pre.next = p.next
            p.next = head
            head = p
            p = pre.next
        else:
            p = p.next
            pre = pre.next
    right = pos.next
    pos.next = None
    if pos == head:
        left = None
    else:
        left = head
        while True:
            if left.next == pos:
                left.next = None
                left = head
                break
            left = left.next

    return left, pos, right




def sortList( head):
    if head is None:
        return None
    if head.next is None:
        return head

    left, right = find_mid(head)
    info(left)
    info(right)
    sorted_left = sortList(left)
    sorted_right = sortList(right)
    head = merge(sorted_left, sorted_right)
    info(head)
    print()
    return head


def merge(h1, h2):
    if h2 is None and h1 is None:
        return None
    elif h1 is None:
        return h2
    elif h2 is None:
        return h1
    else:
        if h1.val <= h2.val:
            head = h1
            h1 = h1.next
        else:
            head = h2
            h2 = h2.next
        p = head
        while True:
            if h1 is None:
                p.next = h2
                break
            if h2 is None:
                p.next = h1
                break
            if h1.val <= h2.val:
                p.next = h1
                p = p.next
                h1 = h1.next
            else:
                p.next = h2
                p = p.next
                h2 = h2.next

    return head


def find_mid(head):
    slow = head
    fast = head
    if head is None:
        return None, None
    elif head.next is None:
        return head, None
    elif head.next.next is None:
        right = head.next
        head.next = None
        return head, right
    else:
        while True:
            if fast is None or fast.next is None:
                right = slow.next
                slow.next = None
                left = head
                break
            slow = slow.next
            fast = fast.next.next
        return left, right

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)

n7.next = n1
n1.next = n3
n3.next = n2
n2.next = n6
n6.next = n5
n5.next = n8
info(n7)
n7 = sortList(n7)
info(n7)
