# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 16:07:24 2021

@author: Lenovo
"""

def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        while True:
            if fast is None:
                return slow
            if fast.next is None:
                return slow
            slow = slow.next
            fast = fast.next.next