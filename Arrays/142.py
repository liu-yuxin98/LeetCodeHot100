# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 23:44:14 2021

@author: Lenovo
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# def detectCycle(head):
#     """
#     :type head: ListNode
#     :rtype: ListNode
#     """

#     if head is None:
#         return None
#     fast = head
#     slowpos = 0
#     slow = head
#     fastpos = 0
#     while True:
#         if fast.next is None:
#             return None
#         if fast == slow and slowpos != fastpos:
#             # there is cycle
#             new_start = head
#             while True:
#                 if slow == new_start:
#                     return slow
#                 slow = slow.next
#                 new_start = new_start.next
#         if fast.next.next == None:
#             return None
#         else:
#             fast =  fast.next.next
#             fastpos += 2
#             slow = slow.next
#             slowpos += 1


def detectCycle(head):
    if head is None:
        return None
    fast = head
    slow = head
    fastpos = slowpos = 0
    while True:
        if fast is None:
            return None
        if fast.next is None:
            return None
        if fast == slow and fastpos != slowpos:
            # not at beginning there is a cycle
            new_start = head
            while True:
                if new_start == slow:
                    return slow
                new_start = new_start.next
                slow = slow.next
        fast = fast.next.next
        slow = slow.next
        fastpos += 2
        slowpos += 1
        
                    
            
            
    