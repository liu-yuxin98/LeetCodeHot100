public class validateBST98 {
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
    public boolean isValidBST(TreeNode root) {
        if(root == null){
            return true;
        }
        if(root.right == null &&root.left == null){
            return true;
        }
        else if(root.right == null){
            TreeNode pre = getPredecessor(root);
            if(pre.val < root.val){
                return isValidBST(root.left);
            }else{
                return false;
            }
        }
        else if(root.left == null){
            TreeNode succ = getSuccessor(root);
            if(succ.val > root.val){
                return isValidBST(root.right);
            }else{
                return false;
            }
        } else{
            TreeNode pre = getPredecessor(root);
            TreeNode succ = getSuccessor(root);
            if(pre.val < root.val && succ.val > root.val){
                return isValidBST(root.left) && isValidBST(root.right);
            } else{
                return false;

            }
        }
    }
}
