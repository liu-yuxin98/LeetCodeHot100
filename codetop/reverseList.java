package codetop;

public class reverseList {

    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode pre = head;
        ListNode cur = head.next;
        ListNode next;
        pre.next = null;
        while (true) {
            next = cur.next;
            cur.next = pre;
            pre = cur;
            if (next == null) {
                return cur;
            }
            cur = next;
        }
    }
}
