public class deleteNodeinBST450 {

    private TreeNode getPredecessor(TreeNode root){
        TreeNode temp = root.left;
        if(temp==null){
            return root;
        }
        while(true){
            if(temp.right == null){
                return temp;
            }
            temp = temp.right;
        }
    }

    public TreeNode deleteNode(TreeNode root, int key) {
        if(root == null){
            return null;
        }
        if(root.val==key){
            if(root.right == null){
                return root.left;
            }else{
                TreeNode pre = root.right;
                TreeNode preParent = root.right;
                if(pre.left == null){
                    pre.left = root.left;
                    return pre;
                }
                pre = pre.left;
                while(true){
                    if(pre.left == null){
                        root.val = pre.val;
                        preParent.left = pre.right;
                        break;
                    }
                    preParent = pre;
                    pre = pre.left;
                }
            }
        }    else if(root.val > key){
            root.left = deleteNode(root.left,key);
        }    else{
            root.right = deleteNode(root.right,key);
        }
        return root;
    }
}
