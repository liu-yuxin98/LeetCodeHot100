public class balancedBinaryTree110 {
    private int countLayer(TreeNode root, Integer depth){
        if(root==null){
            return depth;
        }
        return Math.max(countLayer(root.left,depth+1), countLayer(root.right,depth + 1));
    }
    
    private boolean balancedHelper(TreeNode root){
        if(root==null){
            return true;
        }
        Integer left = countLayer(root.left,0);
        Integer right = countLayer(root.right,0);
        if(Math.abs(left-right)>1){
            return false;
        }
        return balancedHelper(root.left)&&balancedHelper(root.right) ;
        
    }
    
    public boolean isBalanced(TreeNode root) {
        return balancedHelper(root);
    }
}
