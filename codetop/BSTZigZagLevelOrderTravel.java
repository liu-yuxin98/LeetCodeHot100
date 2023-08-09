package codetop;

import com.sun.source.tree.Tree;

import java.util.*;

public class BSTZigZagLevelOrderTravel {

    public List<List<Integer>> zigzagLevelOrder2(TreeNode root) {
        Deque<TreeNode> queue = new LinkedList<>();
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) {
            return res;
        }
        int layer = 0;  // layer%2==1  right to left
        queue.add(root);
        while (queue.size() > 0) {
            int len = queue.size();
            res.add(new ArrayList<>());
            // go through this layer
            for (int i = 0; i < len; i++) {
                TreeNode currentNode = queue.removeFirst();
                res.get(layer).add(currentNode.val);
                if (layer % 2 == 0) {
                    if (currentNode.left != null) {
                        queue.add(currentNode.left);
                    }
                    if (currentNode.right != null) {
                        queue.add(currentNode.right);
                    }
                } else {
                    if (currentNode.right != null) {
                        queue.add(currentNode.right);
                    }
                    if (currentNode.left != null) {
                        queue.add(currentNode.left);
                    }
                }
            }
            reverseDeque(queue);
            layer += 1;
        }
        return res;
    }

    public void reverseDeque(Deque<TreeNode> deque) {
        Deque<TreeNode> tempDeque = new ArrayDeque<>();
        while (!deque.isEmpty()) {
            tempDeque.addLast(deque.removeLast());
        }
        while (!tempDeque.isEmpty()) {
            deque.add(tempDeque.removeFirst());
        }
    }


    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        Deque<TreeNode> queue = new LinkedList<>();
        Deque<TreeNode> queueNext = new LinkedList<>();
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) {
            return res;
        }
        int layer = 0;  // layer%2==1  right to left
        queue.add(root);
        res.add(new ArrayList<>());
        while (true) {
            TreeNode currentNode = queue.removeLast();
            if (currentNode != null) {
                res.get(layer).add(currentNode.val);
                if (layer % 2 == 0) {
                    queueNext.add(currentNode.left);
                    queueNext.add(currentNode.right);
                } else {
                    queueNext.add(currentNode.right);
                    queueNext.add(currentNode.left);
                }
            }
            if (queue.size() == 0) {
                // to next layer
                if (queueNext.size() == 0) {
                    res.remove(layer);
                    break;
                }
                res.add(new ArrayList<>());
                layer += 1;
                //clone value of queueNext to queue
                queue.addAll(queueNext);
                queueNext = new LinkedList<>();
            }
        }
        return res;

    }
}
