class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pHead1 ListNode类
# @param pHead2 ListNode类
# @return ListNode类
#


class Solution:
    def Merge(self, pHead1: ListNode, pHead2: ListNode) -> ListNode:
        # write code here
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1

        p1 = pHead1
        p2 = pHead2
        if pHead1.val <= pHead2.val:
            p = pHead1
            p1 = p1.next
        else:
            p = pHead2
            p2 = p2.next

        cur = p
        while True:
            if p1 is None:
                cur.next = p2
                break
            if p2 is None:
                cur.next = p1
                break
            if p1.val <= p2.val:
                cur.next = p1
                p1 = p1.next
                cur = cur.next
            else:
                cur.next = p2
                p2 = p2.next
                cur = cur.next
        return p
