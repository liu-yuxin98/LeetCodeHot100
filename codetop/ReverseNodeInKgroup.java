package codetop;

import java.util.List;

public class ReverseNodeInKgroup {

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

    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode sentinel = new ListNode();
        sentinel.next = head;
        // count length of head
        int len = countLength(head);
        int t = len / k;
        ListNode front = head;
        ListNode end = findEnd(front, k);
        ListNode prefront = sentinel;
        if (t == 0 || k == 1) {
            return sentinel.next;
        } else {
            for (int i = 0; i < t; i++) {
                if(i == t - 1) {
                    ListNode nextFront = end.next;
                    reverseHelper(prefront, front, end);
                    front.next = nextFront;
                } else {
                    ListNode nextFront = end.next;
                    reverseHelper(prefront, front, end);
                    prefront = front;
                    front = nextFront;
                    end = findEnd(front, k);
                }
            }

        }
        return sentinel.next;
    }

    public int countLength(ListNode head) {
        ListNode temp = head;
        int len = 0;
        while (temp != null) {
            len += 1;
            temp = temp.next;
        }
        return len;
    }

    public ListNode findEnd(ListNode front, int k) {
        // find end node of a segment with length of k from front
        ListNode end = front;
        for (int i = 0; i < k - 1; i++) {
            end = end.next;
        }
        return end;
    }

    public void reverseHelper(ListNode preFront, ListNode front, ListNode end) {
        // reverse from front to end and then let preFront points to end
        reverse(front, end);
        preFront.next = end;
    }

    public void reverse(ListNode front, ListNode end) {
        // reverse from front to end
        ListNode pre = front;
        ListNode cur = front.next;
        pre.next = null;
        if (cur == end) {
            end.next = front;
        } else {
            ListNode next = cur.next;
            while (true) {
                cur.next = pre;
                pre = cur;
                cur = next;
                next = cur.next;
                if (cur == end) {
                    cur.next = pre;
                    break;
                }
            }
        }
    }

    public static void main(String[] args) {


    }
}
