class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead == None or pHead.next == None:
            return pHead

        front = pHead
        # iterate front.val != front.next.val
        while front.next:
            if front.next.val != front.val:
                break
            else:
                front = front.next
        if front.next is None:
            return None

        pHead = front
        back = front.next
        while back:
            if back.next is None:
                break
            else:
                if back.next.val != back.val:
                    front = back
                    back = back.next
                else:
                    while True:
                        if back.next is None:
                            front.next = None
                            break
                        if back.next.val == back.val:
                            back = back.next
                        else:
                            back = back.next
                            front.next = back
                            break
        return pHead
