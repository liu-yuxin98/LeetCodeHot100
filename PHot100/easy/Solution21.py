
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution21:
    def mergeTwoLists(self, l1:ListNode, l2:ListNode)->ListNode:
        res = ListNode(0,None)
        p = res
        p1 = l1
        p2 = l2
        if p1 == None and p2 == None:
            res = None
            return res
        while(p1!=None or p2!=None):
            if (p1 == None and p2!=None):
                p.val = p2.val
                p2 = p2.next
                while(p2!=None):
                   p.next = ListNode(p2.val,None)
                   p = p.next
                   p2 = p2.next
            elif (p2 == None and p1!=None):
                p.val = p1.val
                p1 = p1.next
                while(p1!=None):
                   p.next = ListNode(p1.val,None)
                   p = p.next
                   p1 = p1.next
            else:
                if(p1.val >= p2.val):
                    p.val = p2.val
                    p2 = p2.next
                else:
                    p.val = p1.val
                    p1 = p1.next

                p.next = ListNode(0,None)
                p = p.next
        return res


n1 = ListNode(4)
n2 = ListNode(2,n1)
l1 = ListNode(1,n2)

n3 = ListNode(4)
n4 = ListNode(3,n3)
l2 = ListNode(1,n4)
s21 = Solution21
s21.mergeTwoLists(s21,l1,l2)
