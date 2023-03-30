class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        fast = pHead
        slow = pHead
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                slow = pHead
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return slow
        return None
