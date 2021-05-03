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


def reverse_linked_list(root):
    # use two pointer
    # https://mp.weixin.qq.com/s?__biz=MzU0ODMyNDk0Mw==&mid=2247488340&idx=1&sn=c3d6adc9f737672aab544931502dda2e&chksm=fb418074cc360962b46cb764068a5818f58bed6a4cd05ef61057823918d95f3a192550f02408&scene=21#wechat_redirect
    head = None
    while root:
        temp = root.next
        root.next = head
        head = root
        root = temp
    return head


l3 = ListNode(3,None)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)

l1 = reverse_linked_list(l1)
while l1:
    print(l1.val)
    l1 = l1.next
    
    
    
