public class swapNodesInPairs24 {
    public ListNode swapPairs(ListNode head) {
        ListNode sentinel = new ListNode();
        sentinel.next = head;
        ListNode pPrev = sentinel;
        ListNode p = head;
        if(p==null){
            return null;
        }
        ListNode pNext = head.next;
        if(pNext==null){
            return sentinel.next;
        }
        while(true){
            ListNode temp = pNext.next;
            pPrev.next = pNext;
            pNext.next = p;
            p.next = temp;

            pPrev = p;
            p = temp;
            System.out.println("------");
            if(p == null || p.next == null){
                return sentinel.next;
            }
            pNext = p.next;
        }
    }
}
