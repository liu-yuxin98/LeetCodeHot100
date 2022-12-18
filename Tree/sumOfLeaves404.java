public class sumOfLeaves404 {

    private int sumLeavesHelper(TreeNode root, Boolean isLeft){
        if(root == null){
            return 0;
        }
        if(root.left == null && root.right == null){
            if(isLeft){
            return root.val;}
            return 0;
        }
        int leftsum = sumLeavesHelper(root.left, true);
        int rightsum = sumLeavesHelper(root.right, false);
        return leftsum+rightsum;

    }
    public int sumOfLeftLeaves(TreeNode root) {
        return sumLeavesHelper(root, false);
    }
}
