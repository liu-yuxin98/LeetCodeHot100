class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        if pHead is None or pHead.next is None:
            return pHead
        sentinel = ListNode(None)
        sentinel.next = pHead
        cur = sentinel

        while True:
            if cur.next is None or cur.next.next is None:
                break
            if cur.next.val == cur.next.next.val:
                repValue = cur.next.val
                p = cur.next.next
                while p and p.val == repValue:
                    p = p.next
                cur.next = p
            else:
                cur = cur.next
        return sentinel.next

    # def deleteDuplication(self, pHead):
    #     sentinel = ListNode()
    #     sentinel.next = pHead
    #     cur = sentinel
    #     while cur.next != None and cur.next.next != None:
    #         if cur.next.val == cur.next.next.val:
    #             temp = cur.next.val
    #             while cur.next != None and cur.next.val == temp:
    #                 cur.next = cur.next.next
    #         else:
    #             cur = cur.next
    #     return sentinel.next
