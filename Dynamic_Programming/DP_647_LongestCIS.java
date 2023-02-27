package Dynamic_Programming;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class DP_647_LongestCIS {
    public int findLengthOfLCIS(int[] nums) {
        // dp[i] max length of CIS end with i
        // formula dp[i] = dp[i-1]+1 if nums[i]>nums[i-1], else dp[i] = 1
        // initial
        // loop sequence
        int [] dp = new int[nums.length];
        Arrays.fill(dp, 1);
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > nums[i-1]) {
                dp[i] = dp[i-1]+1;
            }
        }
        int res = Arrays.stream(dp).max().getAsInt();
        return res;
    }
}
