class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
'''
        if head == None:
            return None
        prev,curr = None,head
        while curr:
            head = curr
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return head
'''
class Solution206:
    def reverseList(self, head):
        if head == None:
            return None
        if head.next == None:
            return head
        rest = self.reverseList(head.next)
        rest.next = head
        return head













