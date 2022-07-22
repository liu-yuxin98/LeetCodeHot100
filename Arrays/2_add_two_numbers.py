# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 21:08:10 2022

@author: yuxin_liu_1998
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1,l2):
        add_one = 0
        p1 = l1
        p2 = l2
        p = ListNode()
        p_add = p
        
        while True:
            if p1 == None:
                while p2:
                    p_add.next = ListNode( (p2.val+add_one)%10 )
                    add_one = (p2.val+add_one)//10
                    p_add = p_add.next
                    p2 = p2.next  
                break                       
            elif p2 == None:
                while p1:
                    p_add.next = ListNode( (p1.val+add_one)%10 )
                    add_one = (p1.val+add_one)//10
                    p_add = p_add.next
                    p1 = p1.next     
                break
            else:
                p_add.next = ListNode( (p1.val+p2.val+add_one)%10 )
                add_one = (p1.val+p2.val+add_one)//10
                p_add = p_add.next
                p1 = p1.next
                p2 = p2.next
        if add_one:
            p_add.next = ListNode(1)
        return p.next
