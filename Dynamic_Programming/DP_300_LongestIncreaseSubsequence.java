package Dynamic_Programming;

import java.util.Arrays;
import java.util.Collections;

public class DP_300_LongestIncreaseSubsequence {
    public int lengthOfLIS(int[] nums) {
        // (1) meaning of dp[i] longest IS end with i
        // (2) formula dp[i] = ...
        // (3) initialization
        // (4) loop sequence
        // (5) case test
        int [] dp = new int[nums.length];
        Arrays.fill(dp, 1);
        for(int i = 1; i < nums.length; i++){
            for(int j = 0; j < i; j++){
                if(nums[j]<nums[i]){
                    dp[i] = Math.max(dp[j]+1,dp[i]);
                }
            }

        }
        System.out.println(Arrays.toString(dp));
        int max = 0;
        for (int i = 0; i < dp.length; i++) {
            max = Math.max(dp[i],max);
        }

        return max;

    }
}
