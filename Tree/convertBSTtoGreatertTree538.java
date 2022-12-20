public class convertBSTtoGreatertTree538 {

    private int helper(TreeNode root, int val){
        // return val of root after sum
        if(root == null){
            return val;
        }

        int sucVal = helper(root.right, val);

        root.val += sucVal;
        helper(root.left, root.val);

        if(root.left==null){
            return root.val;
        }else{
            // return value of the left most child of root
           TreeNode temp = root.left;
           while(temp.left!=null){
               temp = temp.left;
           }
           return temp.val;
        }

    }

    public TreeNode convertBST(TreeNode root) {
            helper(root,0);
            return root;
    }
}
