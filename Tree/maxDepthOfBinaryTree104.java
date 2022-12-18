

public class maxDepthOfBinaryTree104 {
    public int maxDepth(TreeNode root) {
        return maxDepthHelper(root,0);
    }
    public int maxDepthHelper(TreeNode root, Integer depth){
        if(root==null){
            return depth;
        }
        return Math.max(maxDepthHelper(root.left, depth+1), maxDepthHelper(root.right, depth+1));
    }
}
