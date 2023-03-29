class Solution:
    def printListFromTailToHead(self, listNode) -> list[int]:
        # write code here
        res = []
        p = listNode
        while p:
            res.append(p.val)
            p = p.next
        return res
