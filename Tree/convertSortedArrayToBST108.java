import java.util.Arrays;

public class convertSortedArrayToBST108 {
    public TreeNode sortedArrayToBST(int[] nums) {
        if(nums.length == 0){
            return null;
        }
        int mid = nums[nums.length/2];
        int [] left = Arrays.copyOfRange(nums,0, nums.length/2 );
        int [] right = Arrays.copyOfRange(nums,nums.length/2 + 1,nums.length);
        TreeNode root = new TreeNode(mid);
        root.left = sortedArrayToBST(left);
        root.right = sortedArrayToBST(right);
        return root;
    }
}
