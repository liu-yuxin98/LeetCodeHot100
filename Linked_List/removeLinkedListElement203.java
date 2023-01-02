public class removeLinkedListElement203 {
    public ListNode removeElements(ListNode head, int val) {
        ListNode sentinel = new ListNode(0);
        sentinel.next = head;
        ListNode pre = sentinel;
        ListNode cur = head;
        while(cur != null){
            if(cur.val == val){
                pre.next = cur.next;
            }else{
                pre = cur;
            }
            cur = cur.next;
        }
        return  sentinel.next;

    }

//    public ListNode removeElements(ListNode head, int val) {
//
//        while(head!=null && head.val==val){
//            head = head.next;
//        }
//        ListNode p = head;
//        ListNode pre = head;
//        if(p==null){
//            return null;
//        }
//        p = p.next;
//        while(p!=null){
//            if(p.val == val){
//                pre.next = p.next;
//            }else{
//                pre = pre.next;
//            }
//            p = p.next;
//        }
//        return head;
//    }

}
