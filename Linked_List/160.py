# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 18:25:26 2021

@author: Lenovo
"""

def getIntersectionNode(self, headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    if headA is None or headB is None:
        return None
    pa = headA
    lenA = 1
    while True:
        if pa.next is None:
            break
        pa = pa.next
        lenA += 1
    pb = headB
    lenB = 1
    while True:
        if pb.next is None:
            break
        pb = pb.next
        lenB += 1
    if pa != pb:
        return None
    pa = headA
    pb = headB
    if lenB <= lenA:
        diff = lenA - lenB
        for i in range(diff):
            pa = pa.next
    else:
        diff = lenB - lenA
        for i in range(diff):
            pb = pb.next

    while True:
        if pa == pb:
            return pa
        pa = pa.next
        pb = pb.next
        
    
        
        
        
    