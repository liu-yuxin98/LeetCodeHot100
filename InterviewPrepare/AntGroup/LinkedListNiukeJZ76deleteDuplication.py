class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return pHead
        pdict = dict()
        p = pHead
        while p:
            pdict[p.val] = pdict.get(p.val, 0)+1
            p = p.next

        p = pHead
        # find first p that are not replication
        while p:
            if pdict[p.val] == 1:
                pHead = p
                break
            p = p.next

        front = pHead
        back = pHead.next
        while True:
            if back is None:
                break
            if pdict[back.val] > 1:
                back = back.next
            else:
                front.next = back
                front = back
                back = back.next
        return pHead
