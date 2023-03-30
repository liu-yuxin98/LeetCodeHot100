class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here

        if pHead is None:
            return None

        # insert node after each node with same label
        cur = pHead
        while cur:
            clone = RandomListNode(cur.label)
            clone.next = cur.next
            cur.next = clone
            cur = clone.next

        # add random node to each copied node
        cur = pHead
        while cur:
            clone = cur.next
            if cur.random is not None:
                clone.random = cur.random.next
            cur = clone.next

        # split
        cur = pHead
        cloneHead = pHead.next

        while cur.next:
            next = cur.next
            cur.next = next.next
            cur = next

        return cloneHead
