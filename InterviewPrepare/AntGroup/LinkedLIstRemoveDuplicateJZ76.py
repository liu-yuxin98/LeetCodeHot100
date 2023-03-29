class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        sentinel = ListNode()
        sentinel.next = pHead
        cur = sentinel
        while cur.next != None and cur.next.next != None:
            if cur.next.val == cur.next.next.val:
                temp = cur.next.val
                while cur.next != None and cur.next.val == temp:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return sentinel.next
