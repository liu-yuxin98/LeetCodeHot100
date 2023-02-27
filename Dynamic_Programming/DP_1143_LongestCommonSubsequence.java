package Dynamic_Programming;

import java.util.Arrays;

public class DP_1143_LongestCommonSubsequence {
    public int longestCommonSubsequence(String text1, String text2) {
        // (1) dp[i][j] length of longest common subsequence in text1[0:i+1], text2[0:j+1]
        // (2) dp[i][j] formula
        // (3) initial
        // (4) loop sequence
        // (5) case study
        int m = text1.length();
        int n = text2.length();
        int [][] dp = new int[m][n];
        // inital
        for (int i = 0; i < m; i++) {
            if(text1.charAt(i) == text2.charAt(0)){
                for (int j = i; j < m; j++) {
                    dp[j][0] = 1;
                }
                break;
            }
        }
        for (int j = 0; j < n; j++) {
            if(text1.charAt(0) == text2.charAt(j)){
                for (int i = j; i < n; i++) {
                    dp[0][i] = 1;
                }
                break;
            }
        }
        //
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (text1.charAt(i) == text2.charAt(j)) {
                    dp[i][j] = dp[i-1][j-1]+1;
                }else{
                    dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
                }
            }
        }
        System.out.println(Arrays.deepToString(dp));

        return dp[m-1][n-1];
    }
}
