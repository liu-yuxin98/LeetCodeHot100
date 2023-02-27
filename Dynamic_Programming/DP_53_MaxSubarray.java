package Dynamic_Programming;

import java.util.Arrays;

public class DP_53_MaxSubarray {
    public int maxSubArray(int[] nums) {
        // (1) dp[i][j]  largest sum subarray end in nums[i]
        // (2) formula
        // (3) initial dp[0] = max(0,nums[0])
        // (4) loop sequence
        // (5) case
        int [] dp = new int[nums.length];
        dp[0] = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if(dp[i-1]<0){
                dp[i] = nums[i];
            }   else{
                dp[i] = dp[i-1]+nums[i];
            }
        }
        return Arrays.stream(dp).max().getAsInt();
    }
}
