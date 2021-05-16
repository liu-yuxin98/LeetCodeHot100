# -*- coding: utf-8 -*-
"""
Created on Sun May 16 17:09:39 2021

@author: Lenovo
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    fast = head
    slow = head
    i = 0
    while True:
        fast = fast.next
        i += 1
        if i >= n:
            break
    if fast is None:
        head = head.next
        return head
    else:
        while True:
            if fast.next is None:
                if n == 1:
                    slow.next = None
                else:
                    slow.next = slow.next.next
                break
            fast = fast.next
            slow = slow.next
        return head

