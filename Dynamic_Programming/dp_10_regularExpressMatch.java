package Dynamic_Programming;

import java.lang.reflect.Array;
import java.util.Arrays;

public class dp_10_regularExpressMatch {
    public boolean isMatch(String s, String p) {
        // dp[i][j] s[0:i] matches p[0:j] or not
        // formula
        // initial
        // loop
        // case
        int m = s.length();
        int n = p.length();
        boolean [][] dp = new boolean[m+1][n+1];
       for (int i = 0; i < m+1; i++) {
           for (int j = 0; j < n+1; j++) {
               dp[i][j] = false;
           }
       }
        dp[0][0] = true;

        for (int i = 0; i < m+1; i++) {
            for (int j = 1; j < n+1; j++) {
                if(p.charAt(j-1)=='*'){
                    //dp[i][j-2] -> s[0:i] matches p[0:j-2] 相当于忽略 p[j-2:j] 比如aab, c*a*b 忽略 c*
                    // dp[i-1][j] -> s[0:i-1] matches p[0:j] 且 s[i-1] = p[j-2] or p[j-2] = .
                    dp[i][j] = dp[i][j-2] || (i>0 && dp[i-1][j] && (s.charAt(i-1)==p.charAt(j-2) || p.charAt(j-2)=='.'));
                }else{
                    dp[i][j] = i>0 && dp[i-1][j-1] && ( s.charAt(i-1)==p.charAt(j-1) || p.charAt(j-1)=='.');
                }
            }
        }
        System.out.println(Arrays.deepToString(dp));
        return dp[m][n];
    }
}
