package Dynamic_Programming;

import java.util.Arrays;

public class TargetSum494 {
    public int findTargetSumWays(int[] nums, int target) {
        int sum = Arrays.stream(nums).sum();

        if(target < 0 && sum+target<0){
            return 0;
        }
        if((target+sum)%2!=0){
            return 0;
        }

        int bagSize = (target+sum)/2;
        if(bagSize<0){
            bagSize = -bagSize;
        }
        int [] dp = new int[bagSize+1];
        dp[0]=1;
        for(int i=0;i< nums.length;i++){
            for(int j = bagSize; j >=nums[i]; j--){
                dp[j] += dp[j-nums[i]];
            }
        }
        return dp[bagSize];
    }
}
