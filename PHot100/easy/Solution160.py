class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution160:
    def getIntersectionNode(self, headA, headB):
        if headA == None or headB == None:
            return 'No intersection'


