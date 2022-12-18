public class symmetricTree101 {


    public boolean isSymmetric(TreeNode root) {
        if(root == null){
            return true;
        }
        return symmetricHelper(root.left,root.right);
    }

    private boolean symmetricHelper(TreeNode root1, TreeNode root2){
        if(root1==null && root2 == null){
            return true;
        }
        if( (root1 == null && root2 != null) ||(root1 != null && root2 == null)) {
            return false;
        }
        if(root1.val == root2.val){
            return symmetricHelper(root1.left,root2.right) && symmetricHelper(root1.right,root2.left);
        }else{
            return false;
        }
    }
}
