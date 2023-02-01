package Dynamic_Programming;

import java.util.Arrays;

public class TargetSum494 {
    public int findTargetSumWays(int[] nums, int target) {

       int sum = Arrays.stream(nums).sum();

       if((sum+target)%2!=0){
           return 0;
       }

       int left = (sum+target)/2;
       if(left<0){
           left = -left;
       }
       int [] dp = new int[left+1];
       dp[0] =1;
       for (int i = 0; i < nums.length; i++) {
           for(int j=left;j>=nums[i];j--){
               dp[j] = dp[j-nums[i]]+dp[j];
           }
       }
       return dp[left];
    }
}
