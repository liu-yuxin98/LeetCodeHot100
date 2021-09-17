# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 09:32:49 2021

@author: Lenovo
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def removeNthFromEnd(self, head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    p = head
    length = 1
    while True:
        if p.next is None:
            break
        p = p.next
        length += 1
    print(length)
    if length == n:
        head = head.next
    else:
        p = head
        pos = 1
        while True:
            if pos >= length - n:
                break
            p = p.next
            pos += 1

        if n == 1:
            p.next = None
        else:
            removed = p.next
            p.next = removed.next
    return head
    
    