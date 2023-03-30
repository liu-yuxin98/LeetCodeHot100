class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def ReverseList(self, head) -> ListNode:
        # write code here
        if head is None or head.next is None:
            return head
        p = head
        cur = p.next

        while cur:
            nextCur = cur.next
            cur.next = p
            p = cur
            cur = nextCur
        return p
