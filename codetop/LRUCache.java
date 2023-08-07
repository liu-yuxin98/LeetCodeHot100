package codetop;

import java.util.Deque;
import java.util.HashMap;
import java.util.LinkedList;

//public class LRUCache {
//          TLE
//
//        private int size =0;
//        private int capacity;
//        private HashMap<Integer,Integer> map = new HashMap<Integer, Integer>();
//        private Deque<Integer> queue = new LinkedList<>();
//
//        public LRUCache(int capacity) {
//            this.capacity = capacity;
//        }
//
//        public int get(int key) {
//            if(map.containsKey(key)){
//                queue.addLast(key);
//                return map.get(key);
//            }else{
//                return -1;
//            }
//        }
//
//        public void put(int key, int value) {
//            if(map.containsKey(key)){
//                queue.addLast(key);
//                map.put(key, value);
//            }
//            else if(size<capacity){
//                queue.add(key);
//                map.put(key, value);
//                size++;
//            }else{
//                //need to pop least recently used cache
//                int popkey = queue.removeFirst();
//                while(queue.contains(popkey)){
//                    popkey = queue.removeFirst();
//                }
//                map.remove(popkey);
//                map.put(key, value);
//                queue.addLast(key);
//            }
//        }
//
//}

public class LRUCache {
    private int size = 0;
    private int capacity;
    private Node sentinel = new Node(-1, -1);
    private HashMap<Integer, Node> map = new HashMap<Integer, Node>();

    public LRUCache(int capacity) {
        this.capacity = capacity;
        sentinel.next = sentinel;
        sentinel.prev = sentinel;
    }

    public int get(int key) {
        if (map.containsKey(key)) {
            //update node
            Node node = map.get(key);
            //remove node
            removeNode(node);
            // append it to end of deque
            appendTail(node);
            return node.val;
        }
        return -1;
    }

    public void removeNode(Node node) {
        Node pre = node.prev;
        Node next = node.next;
        pre.next = next;
        next.prev = pre;
        node.prev = null;
        node.next = null;
    }

    public void appendTail(Node node) {
        Node tail = sentinel.prev;
        tail.next = node;
        node.prev = tail;
        sentinel.prev = node;
        node.next = sentinel;
    }

    public void put(int key, int value) {
        if (map.containsKey(key)) {
            // remove pre node
            Node node = map.get(key);
            removeNode(node);
            size--;
        } else if (size >= capacity) {
            // remove least used cache
            Node lruNode = sentinel.next;
            removeNode(lruNode);
            map.remove(lruNode.key);
        }
        Node node = new Node(key, value);
        map.put(key, node);
        appendTail(node);
        size++;
    }

    class Node {
        Node prev;
        Node next;
        int key;
        int val;

        public Node(int key, int val) {
            this.key = key;
            this.val = val;
        }
    }

    public static void main(String[] args) {
        LRUCache lru = new LRUCache(2);
        lru.put(1,0);
        lru.put(2,2);
        lru.get(1);
        lru.put(3,3);
        lru.get(2);
        lru.put(4,4);
        lru.get(1);
        lru.get(3);
        lru.get(4);

    }
}