class Solution:
    def removeElements(self, head, val: int):
        # loop till head.val != val
        while head != None:
            if head.val != val:
                break
            head = head.next
        # head.val != val or head is None
        if head is None:
            return None

        pre = head
        cur = head.next
        while cur:
            if cur.val == val:
                pre.next = cur.next
                cur = pre.next
            else:
                pre = pre.next
                cur = cur.next
        return head
