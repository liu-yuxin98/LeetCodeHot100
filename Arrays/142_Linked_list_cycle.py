# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 11:36:15 2022

@author: yuxin_liu_1998
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def detectCycle(head:ListNode) -> ListNode:
        slow = head
        fast = head
        step = 0
        while True:
            if fast is None:
                return None
            elif fast.next is None:
                return None
            
            if slow == fast and step!=0:   # must contain cycle
                fast = head
                while True:
                    if fast == slow:
                        return slow
                    fast = fast.next
                    slow = slow.next
                    
            slow = slow.next
            fast = fast.next.next
            step += 1


l = ListNode(3)
l.next = ListNode(2)
l.next.next = ListNode(0)
l.next.next.next = ListNode(-4)
l.next.next.next.next = l.next


t = detectCycle(l)
print(t.val)

