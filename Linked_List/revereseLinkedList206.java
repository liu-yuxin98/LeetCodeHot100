public class revereseLinkedList206 {
    public ListNode reverseList(ListNode head) {
        if(head==null){
            return null;
        }
        ListNode p = head;
        ListNode nextH = head.next;
        while(nextH != null){
            ListNode temp = nextH;
            nextH = nextH.next;
            temp.next = head;
            head = temp;
        }
        p.next = null;
        return head;
    }
}
