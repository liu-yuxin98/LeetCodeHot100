# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 19:06:08 2021

@author: Lenovo
"""

def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head is None:
        return None
    temp_head = head
    cur_head = head
    next_head = temp_head.next
    temp_head.next = None
    while next_head:
        temp_head = next_head
        next_head = temp_head.next
        temp_head.next = cur_head
        cur_head = temp_head
    head = cur_head
    return head
