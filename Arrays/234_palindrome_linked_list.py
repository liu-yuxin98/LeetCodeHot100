# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 14:16:17 2022

@author: yuxin_liu_1998
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def isPalindrome(head: ListNode) -> bool:
        # find mid point of the list
        slow = head
        fast = head
        # special cases len = 1
        if slow.next is None:
            return True
        # decide the len of list is odd or even
        is_odd = True
        while True:
            if fast.next is None: # len list is odd
                break
            if fast.next.next is None: # len list is even
                is_odd = False
                break
            slow = slow.next
            fast = fast.next.next
        mid = slow    # mid points to pos (len-1)//2
        
        # reverse the front half
        p = head.next     
        p_pre = head
        p_pre.next = None
        
        while True:
            if is_odd:
                if p == mid:
                    break
            else:
                if p_pre == mid:
                    break
            p_next = p.next
            p.next = p_pre
            p_pre = p
            p = p_next   
        # p_left point to the left half and p_right point to the right half
        p_left = p_pre
        if is_odd:
            p_right = p.next
        else:
            p_right = p
        # check palindrome
        while True:
            if p_left is None or p_right is None:
                break
            if p_left.val != p_right.val:
                return False
            p_left = p_left.next
            p_right = p_right.next
        return True
            
        
        
        
    

l = ListNode(0)
l.next = ListNode(1)
l.next.next = ListNode(1)
l.next.next.next = ListNode(1)
l.next.next.next.next = ListNode(1)
l.next.next.next.next.next = ListNode(0)
out = isPalindrome(l)


        
