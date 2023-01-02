public class removeNthNodeFromEnd19 {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int length = 0;
        ListNode sentinel = new ListNode();
        sentinel.next = head;
        ListNode p = head;
        while(p!=null){
            p = p.next;
            length ++;
        }
        p = sentinel;
        for(int i=0;i<length-n;i++){
            p = p.next;
        }
        p.next = p.next.next;
        return sentinel.next;
    }
}
