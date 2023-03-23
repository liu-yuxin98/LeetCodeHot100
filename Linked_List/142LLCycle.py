class Solution:
    def detectCycle(self, head):
        if head == None:
            return None
        fast = head
        slow = head

        while True:
            if fast is None:
                return None
            elif fast.next is None:
                return None
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                temp = head
                while True:
                    if temp == fast:
                        return fast
                    temp = temp.next
                    fast = fast.next
