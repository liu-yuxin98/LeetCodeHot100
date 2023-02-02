package Dynamic_Programming;

import java.util.Arrays;

public class CombinationSum377 {
    public int combinationSum4(int[] nums, int target) {
        int [] dp = new int[target+1];
        dp[0] = 1;
        for(int i=1;i<dp.length;i++){
            for(int j=0;j< nums.length;j++){
                // can not fit
                if(nums[j]>i){
                    continue;
                } else{
                    // nums[j] can fit into bag
                    dp[i] += dp[i-nums[j]];
                }
            }
        }
        return dp[target];
    }
}
