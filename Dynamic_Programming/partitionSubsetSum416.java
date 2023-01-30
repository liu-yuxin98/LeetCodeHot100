package Dynamic_Programming;

import java.util.Arrays;

public class partitionSubsetSum416 {
    public boolean canPartition(int[] nums) {

        int sum = Arrays.stream(nums).sum();
        if(sum%2==1){
            return false;
        }
        int [] dp = new int[sum/2+1];
        for (int i = 0; i < nums.length;i++) {
            for(int j=sum/2;j>=nums[i];j--){
                dp[j] = Math.max(dp[j],dp[j-nums[i]]+nums[i]);
            }
        }

        return dp[sum/2]==sum/2;
    }

}
