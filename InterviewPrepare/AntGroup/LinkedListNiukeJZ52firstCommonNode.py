# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
#
# @param pHead1 ListNode类
# @param pHead2 ListNode类
# @return ListNode类
#
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if pHead1 is None or pHead2 is None:
            return None

        p1 = pHead1
        len1 = 0
        while p1:
            if p1.next is None:
                len1 += 1
                break
            p1 = p1.next
            len1 += 1

        p2 = pHead2
        len2 = 0
        while p2:
            if p2.next is None:
                len2 += 1
                break
            p2 = p2.next
            len2 += 1

        if p1 == p2:
            p1 = pHead1
            p2 = pHead2
            if len1 >= len2:
                for _ in range(len1-len2):
                    p1 = p1.next
            else:
                for _ in range(len2-len1):
                    p2 = p2.next

            while p1 != p2:
                p1 = p1.next
                p2 = p2.next
            return p1

        else:
            return None
