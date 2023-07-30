import java.util.Arrays;
import java.util.Collections;

public class maximuSubarray_53 {
//    public static int maxSubArray(int[] nums) {
//        // dynamic programming
//        Integer[] dp = new Integer[nums.length];
//        dp[0] =nums[0];
//        for(int i = 1; i < nums.length; i++){
//            dp[i] = Math.max(dp[i-1],0)+nums[i];
//        }
//
//        int max = Collections.max(Arrays.asList(dp)) ;
//        return max;
//    }
    public static int maxSubArray(int[] nums) {
        // Greedy algorithm
        int cur_sum = 0;
        int max = nums[0];
        for(int i = 0; i < nums.length; i++){
            cur_sum += nums[i];
            max = Math.max(max,cur_sum);
            if(cur_sum<0){
                cur_sum = 0;
            }
        }
        return max;
    }

}
