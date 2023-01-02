public class ListNode {
    int val;
    ListNode next;
    ListNode pre;
    ListNode(){};

    public ListNode(int val) {
        this.val = val;
    }
    ListNode(int val, ListNode pre,ListNode next){this.val = val; this.next = next;this.pre = pre;}

}
