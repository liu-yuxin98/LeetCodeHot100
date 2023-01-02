public class IntersectionOfTwoLinkedList160 {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        int lenA = 0;
        int lenB = 0;
        ListNode p = headA;
        while(p!=null){
            p = p.next;
            lenA ++;
        }
        p = headB;
        while (p != null) {
            p = p.next;
            lenB++;
        }
        if(lenA>=lenB){
            while(lenA>lenB){
                headA = headA.next;
                lenA --;
            }
        } else{
          while(lenB>lenA){
              headB = headB.next;
              lenB --;
          }
        }

        while(headA!=null && headB != null){
            if(headA==headB){
                return headA;
            }
            headA = headA.next;
            headB = headB.next;
        }
        return null;
    }
}
