public class minAbsoluteDifferenceInBST530 {

    private TreeNode getPredecessor(TreeNode root){
        TreeNode temp = root.left;
        while(true){
            if(temp.right == null){
                return temp;
            }
            temp = temp.right;
        }

    }
    private TreeNode getSuccessor(TreeNode root){
        TreeNode temp = root.right;
        while(true){
            if(temp.left == null){
                return temp;
            }
            temp = temp.left;
        }

    }
    public int getMinimumDifference(TreeNode root) {
        if(root.left==null && root.right == null){
            return Integer.MAX_VALUE;
        }
        if(root.right == null){
            TreeNode pre = getPredecessor(root);
            int left_min = getMinimumDifference(root.left);
            return Math.min(root.val-pre.val,left_min );

        }
        if(root.left == null){
            TreeNode suc = getSuccessor(root);
            int right_min = getMinimumDifference(root.right);
            return Math.min(suc.val-root.val,right_min );
        }

        TreeNode pre = getPredecessor(root);
        TreeNode suc = getSuccessor(root);
        int val = Math.min(root.val-pre.val, suc.val- root.val);
        int left_min = getMinimumDifference(root.left);
        int right_min = getMinimumDifference(root.right);
        return Math.min(Math.min(val,left_min), right_min);

    }
}
