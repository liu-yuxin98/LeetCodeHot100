class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution141:

    def hasCycle(self, head):
        headlist = []
        while True:
            if head == None:
                return False
            elif head in headlist:
                return True
            else:
                headlist.append(head)
                head = head.next



