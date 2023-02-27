package Dynamic_Programming;

import java.lang.reflect.Array;
import java.util.Arrays;

public class DP_718_MaxRepeatSubarray {
    public int findLength(int[] nums1, int[] nums2) {
        // dp[i][j] max common sub array length end with nums1[i] ,nums2[j]
        // if nums1[i] == nums2[j], dp[i][j] = dp[i-1][j-1]+1
        // initial ->0
        // loop sequence, 1->n-1
        // case
        int m = nums1.length;
        int n = nums2.length;
        int [][] dp = new int[m][n];
        int max = 0;
        // initial
        for (int i = 0; i < m; i++) {
            if (nums1[i] == nums2[0]) {
                dp[i][0] = 1;
                max = 1;
            }else{
                dp[i][0] = 0;
            }
        }
        for (int j = 0; j < n; j++) {
            if(nums2[j] == nums1[0]){
                dp[0][j] = 1;
                max = 1;
            }
        }
        // loop
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if(nums1[i] == nums2[j]){
                    dp[i][j] = dp[i-1][j-1]+1;
                }
            }
        }


        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                max = Math.max(max, dp[i][j]);
            }
        }

        return max;
    }
}
