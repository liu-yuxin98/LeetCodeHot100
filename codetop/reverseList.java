package codetop;

public class reverseList {
    public class ListNode {
        int val;
        ListNode next;

        ListNode() {
        }

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }

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
