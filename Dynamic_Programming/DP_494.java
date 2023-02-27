package Dynamic_Programming;

import java.util.Arrays;

public class DP_494 {
    public int findTargetSumWays(int[] nums, int target) {
        int sum = Arrays.stream(nums).sum();
        if((sum+target)%2==1){
            return 0;
        }
        int a = (sum+target)/2;
        int [] dp = new int[a+1];
        dp[0] = 1;
        for(int i=0;i<dp.length;i++){
            for(int j=0;j<nums.length; j++){

                if(nums[j]<=i){
                    dp[i] += dp[i-nums[j]];
                }
            }
        }
        return dp[a];
    }
}
