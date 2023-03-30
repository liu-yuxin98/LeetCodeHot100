class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, pHead, k: int):
        # write code here
        length = 0
        sentinel = ListNode(None)
        sentinel.next = pHead
        p = sentinel
        while True:
            p = p.next
            if p is None:
                break
            length += 1
        if k > length:
            return None

        pos = length - k+1
        p = sentinel
        cnt = 0
        while True:
            p = p.next
            cnt += 1
            if cnt == pos:
                return p
