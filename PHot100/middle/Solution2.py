# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0 # decide wheather should add 1 in upper position
        res = ListNode(0) # result
        p = res # point to move along the res
        while (l1!=None or l2!= None):
            newp = ListNode(0)
            if(l1 == None):
               sum = l2.val+carry
               carry = sum //10
               newp.val = sum %10
               l2 = l2.next
            elif l2==None:
                sum = l1.val+carry
                carry = sum//10
                newp.val = sum%10
                l1 = l1.next
            else:
                sum = l1.val+l2.val + carry
                carry = sum // 10
                newp.val = sum % 10
                l1 = l1.next
                l2 = l2.next
            p.next = newp
            p = p.next
        if carry:
            p.next = ListNode(1)
            p = p.next

        return res.next

l1 =  ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(7)
s = Solution
l3 = s.addTwoNumbers(s,l1,l2)









