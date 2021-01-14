import org.junit.Test;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.stream.Collectors;
import static org.junit.Assert.*;
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

public class Solution2 {
     public class ListNode {
      int val;
      ListNode next;
      ListNode(int x) { val = x; }
    }

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
         ListNode p1 = l1;
         ListNode p2 = l2;
         /* careat res*/
         ListNode res = new ListNode(0);
         ListNode p = res;

         while(true){
            int valuei = 0;
            if(p1!=null && p2!=null){
                valuei = p.val +p1.val+ p2.val;
                p1 = p1.next;
                p2 = p2.next;
            } else if(p1 == null && p2!=null){
                valuei = p.val+p2.val;
                p2 = p2.next;
            } else if (p1!=null && p2 ==null){
                valuei = p.val + p1.val;
                p1 = p1.next;
            } else{
                /* p1,p2 == null*/
                break;
            }
            if(valuei<10){
                p.val = valuei;
                if(p1 ==null && p2 == null){
                    break;
                } else{
                    p.next = new ListNode(0);
                    p = p.next;
                }

            } else{
                p.val = valuei-10;
                p.next = new ListNode(1);
                p = p.next;
            }

         }
            return res;

    }


    @Test
    public void Testcases(){
        /* [2,4,3]+[5,6,5]->[7,0,8]*/
        ListNode ld1 = new ListNode(2);
        ld1.next = new ListNode(4);
        ld1.next.next = new ListNode(3);

        ListNode ld2 = new ListNode(5);
        ld2.next = new ListNode(6);
        ld2.next.next = new ListNode(4);

        ListNode actual1 = addTwoNumbers(ld1,ld2);
        ListNode expeted1 = new ListNode(7);
        expeted1.next = new ListNode(0);
        expeted1.next.next = new ListNode(8);
        while(actual1!=null){
            assertEquals(actual1.val,expeted1.val);
            actual1 = actual1.next;
            expeted1 = expeted1.next;
        }
        /* [0]+[0]->[0]*/
        ListNode ld3 = new ListNode(0);
        ListNode ld4 = new ListNode(0);
        ListNode actual2 = addTwoNumbers(ld3,ld4);
        ListNode expeted2 = new ListNode(0);
        assertEquals(expeted2.val,actual2.val);

        /* l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9] */
        ListNode ld5 = new ListNode(9);
        ListNode p5 = ld5;
        for(int i=0;i<6;i++){
            p5.next = new ListNode(9);
            p5 = p5.next;
        }
        ListNode ld6 = new ListNode(9);
        ListNode p6 = ld6;
        for(int i=0;i<3;i++){
            p6.next = new ListNode(9);
            p6 = p6.next;
        }
        ListNode expected3 = new ListNode(8);
        ListNode pe = expected3;
        for(int i=0;i<3;i++){
            pe.next = new ListNode(9);
            pe = pe.next;
        }
        for(int i=0;i<3;i++){
            pe.next = new ListNode(0);
            pe = pe.next;
        }
        pe.next = new ListNode(1);

        ListNode actual3 = addTwoNumbers(ld5,ld6);
        while(actual3!=null){
            assertEquals(actual3.val,expected3.val);
            actual3 = actual3.next;
            expected3 = expected3.next;
        }

    }

}
