public class LinkedListCycle142 {
    public ListNode detectCycle(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;
        while(true){

            if(fast==null || fast.next == null){
                return null;
            }
            slow = slow.next;
            fast = fast.next.next;
            if(fast==slow){
                break;
            }
        }
        ListNode p = head;
        while(true){
            if(p==slow){
                return p;
            }
            p = p.next;
            slow = slow.next;
        }
    }
}
