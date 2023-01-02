public class MyLinkedList {
    ListNode sentinel;
    int length = 0;
    public MyLinkedList() {
        sentinel = new ListNode();
    }

    public int get(int index) {
        if(index>=length){
            return -1;
        }
        ListNode p = sentinel;
        for(int i=0;i<=index; i++){
            p = p.next;
        }
        return p.val;
    }

    public void addAtHead(int val) {
            if(length==0){
                sentinel.next = new ListNode(val,sentinel,sentinel);
                sentinel.pre = sentinel.next;
            }else{
            ListNode preHead = sentinel.next;
            sentinel.next = new ListNode(val,sentinel,preHead);
            preHead.pre = sentinel.next;
            }
            length +=1;
    }

    public void addAtTail(int val) {
        if(length == 0){
            sentinel.next = new ListNode(val,sentinel,sentinel);
            sentinel.pre = sentinel.next;
        }else{
            ListNode pTail = sentinel.pre;
            pTail.next = new ListNode(val, pTail,sentinel);
            sentinel.pre = pTail.next;
        }
        length ++;
    }

    public void addAtIndex(int index, int val) {
        if(index>length || index < 0){
            return;
        } else if(index==length){
            addAtTail(val);
        }  else{
            length++;
            ListNode p = sentinel;
            for(int i=0;i<index;i++){
                p = p.next;
            }
            ListNode indexNode = p.next;
            p.next = new ListNode(val,p,indexNode);
            indexNode.pre = p.next;
        }
    }

    public void deleteAtIndex(int index) {
        if(index < 0 || index >= length){
            return;
        }
        length--;
        ListNode p = sentinel;
        for(int i=0;i<index;i++){
            p = p.next;
        }
        // index == length-1
        if(p.next.next == null){
            p.next = sentinel;
            sentinel.pre = p;
        }else{
         p.next = p.next.next;
         p.next.pre = p;
        }
    }
}
