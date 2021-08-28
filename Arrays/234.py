# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 08:18:51 2021

@author: Lenovo
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    # O（n) time O(1) space
    t = head
    length = 0
    while True:
        if t is None:
            break
        length += 1
        t = t.next

    # reverse front half part of the linked list and mid point to the middle
    next_p = head.next
    head.next = None
    pos = 1
    while True:
        if pos >= length//2:
            mid = next_p
            break
        temp = next_p.next
        next_p.next = head
        head = next_p
        next_p = temp
        pos += 1
    if length % 2 != 0 and length > 1:
        mid = mid.next
    if length == 1:
        mid = head
    # compare mid with new_head
    while True:
        if head is None and mid is None:
            return True
        if head.val != mid.val:
            return False
        head = head.next
        mid = mid.next



head = ListNode(1)
head.next = ListNode(3)
head.next.next = ListNode(1)
# head.next.next.next = ListNode(3)
# head.next.next.next.next = ListNode(2)
# head.next.next.next.next.next = ListNode(1)
res = isPalindrome(head)