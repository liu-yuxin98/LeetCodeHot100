public class invertBinaryTree226 {


    private void invertHelper(TreeNode root){
        if(root == null){
            return;
        }
        if(root.left == null && root.right == null){
            return;
        }
        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;
        invertTree(root.right);
        invertTree(root.left);
    }

    public TreeNode invertTree(TreeNode root) {
         invertHelper(root);
         return root;
    }
}
