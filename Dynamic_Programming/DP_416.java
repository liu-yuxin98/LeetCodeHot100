package Dynamic_Programming;

import java.util.Arrays;

public class DP_416 {
    public boolean canPartition(int[] nums) {
        int sum = Arrays.stream(nums).sum();
        if(sum%2==1) return false;
        if(sum<0) sum=-sum;
        int [] dp = new int[sum/2+1];
        //method 1
        // outer loop->item
        for (int i = 0; i < nums.length; i++) {
            //inner loop -> dp from end to front
            for (int j = dp.length-1; j >= nums[i]; j--) {
                dp[j] = Math.max(dp[j],dp[j-nums[i]]+nums[i]);
            }
        }

        return dp[sum/2]==sum/2;
    }
}
