# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 18:25:26 2021

@author: Lenovo
"""
# double pointer best solution
def getIntersectionNode(self, headA, headB): 
    pa = headA
    pb = headB
    while True:
        if pa is None and pb is None:
            return None
        elif pa is None:
            pa = headB
        elif pb is None:
            pb = headA
        if pa == pb:
            return pa
        pa = pa.next
        pb = pb.next


def getIntersectionNode(self, headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
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
        
# 2021.12.28  
def getIntersectionNode(self, headA, headB):     
        la = 1
        lb = 1
        pa = headA
        pb = headB
        while True:
            if pa.next is None:
                break
            pa = pa.next 
            la += 1
    
        while True:
            if pb.next is None:
                break
            pb = pb.next 
            lb += 1 
        
        ta = headA
        tb = headB
        if lb>la:
            differ = lb -la
            while differ > 0:
                tb  = tb.next
                differ -= 1
        elif lb < la:
            differ = la - lb
            while differ > 0:
                ta  = ta.next
                differ -= 1 
        
        while True:
            if ta == tb:
                return ta
            if ta is None or tb is None:
                return None
            ta = ta.next
            tb = tb.next
            
# hashset
def getIntersectionNode(self, headA, headB): 
    ta = headA
    tb = headB
    hash_set = set()
    while True:
        if ta is None:
            break
        hash_set.add(ta)
        ta = ta.next 
    while True:
        if tb is None:
            return None 
        if tb in hash_set:
            return tb
        tb = tb.next



            