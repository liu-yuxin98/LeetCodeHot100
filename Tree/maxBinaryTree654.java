import java.util.Arrays;
import java.util.stream.IntStream;

public class maxBinaryTree654 {
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        if(nums.length == 0){
            return null;
        }
        if(nums.length == 1){
            return new TreeNode(nums[0]);
        }

        int max = Arrays.stream(nums).max().getAsInt();
        int index = IntStream.range(0,nums.length).filter(i->nums[i]== max).findFirst().orElse(-1);

        int [] leftNums = Arrays.copyOfRange(nums,0,index);
        int [] rightNums = Arrays.copyOfRange(nums, index + 1, nums.length);

        TreeNode r = new TreeNode(max);
        r.left = constructMaximumBinaryTree(leftNums);
        r.right = constructMaximumBinaryTree(rightNums);

        return r;
    }
}
