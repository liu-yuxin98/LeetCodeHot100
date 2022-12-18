public class pathSum112 {

    private boolean pathSumHelper(TreeNode root,Integer curSum, Integer targetSum){
        if(root==null){
            return false;
        }
        if(root.left == null && root.right == null){
            return curSum+ root.val == targetSum;
        }
        curSum = curSum +root.val;
        if(pathSumHelper(root.left, curSum,targetSum)){
            return true;
        }
        if(pathSumHelper(root.right, curSum,targetSum)){
            return true;
        }
        return false;

    }

    public boolean hasPathSum(TreeNode root, int targetSum) {
            return pathSumHelper(root,0,targetSum);
    }
}
