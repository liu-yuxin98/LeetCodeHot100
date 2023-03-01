package Dynamic_Programming;

import java.util.Arrays;

public class dp_72_edit_Dis {
    public int minDistance(String word1, String word2) {
        // dp[i][j] means steps to make word1[0:i] same as word2[0:j]
        // formula if word1[i-1] = word2[j-1]  dp[i][j] = dp[i-1][j-1] else: dp[i][j] = min(dp[i-1][j]+1,dp[i][j-1]+1,
        // initial
        // loop
        // case
        int m = word1.length();
        int n = word2.length();
        int [][] dp = new int[m+1][n+1];
        //
        for(int i = 0; i < m+1; i++){
            dp[i][0] = i;
        }
        for (int j = 0; j < n+1; j++) {
            dp[0][j] = j;
        }

        // loop
        for (int i = 1; i < m+1; i++) {
            for (int j = 1; j < n+1; j++) {
                if(word1.charAt(i-1)==word2.charAt(j-1)){
                    dp[i][j] = dp[i-1][j-1];
                }else{
                    dp[i][j] = Math.min(dp[i-1][j-1], Math.min( dp[i-1][j],dp[i][j-1]))+1;
                }
            }
        }


//        System.out.println(Arrays.deepToString(dp));
        return dp[m][n];
    }
}
