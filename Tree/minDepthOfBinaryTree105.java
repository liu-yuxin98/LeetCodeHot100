public class minDepthOfBinaryTree105 {
    public int minDepth(TreeNode root) {
        return minDepthHelper(root,0);
    }
    public int minDepthHelper(TreeNode root, Integer depth){
        if(root==null){
            return depth;
        } else if(root.left == null && root.right != null){
            return minDepthHelper(root.right, depth + 1);
        } else if(root.left != null && root.right == null){
            return minDepthHelper(root.left, depth + 1);
        }
        return Math.min(minDepthHelper(root.left, depth+1), minDepthHelper(root.right, depth+1));
    }
}
