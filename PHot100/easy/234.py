# -*- coding: utf-8 -*-
"""
Created on Mon May  3 12:24:21 2021

@author: Yuxin Liu
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        values = []
        while head:
            values.append(head.val)
            head = head.next
        invvalues = values[::-1]
        return invvalues == values
