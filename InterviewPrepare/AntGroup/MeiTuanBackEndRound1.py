class ListNode:
    def __init__(self, x) -> None:
        self.val = x
        self.next = None


def insertBehind(head):
    slow = head
    fast = head

    # find mid of the list
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    mid = slow
    # if fast == None:
    #     # list has even number of node, slow points to n/2 + 1 node,node start from 1
    #     pass
    # else:
    #     # list has odd number of node, slow points to (n+1)//2 node, just mid
    #     pass
    # reverese right half
    cur = mid.next
    righthead = mid
    righthead.next = None
    while cur:
        nextCur = cur.next
        cur.next = righthead
        righthead = cur
        cur = nextCur
    # righthead now point to the head of the right half one(reversed)
    leftHead = head
    while leftHead:
        nextLeft = leftHead.next
        nextRight = righthead.next
        leftHead.next = righthead
        leftHead.next.next = nextLeft
        righthead = nextRight
        leftHead = nextLeft


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)


insertBehind(head)

p = head

while p:
    print(p.val)
    p = p.next
