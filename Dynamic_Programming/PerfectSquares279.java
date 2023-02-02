package Dynamic_Programming;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class PerfectSquares279 {
    public int numSquares(int n) {
        List<Integer> squres = new ArrayList<Integer>();
        int num = 1;
        while(num*num<=n){
            squres.add(num*num);
            num+=1;
        }
//        System.out.println(squres);
        int [] dp = new int[n+1];
        Arrays.fill(dp,n+1);
        dp[0] = 0;
        for (int i = 1; i <= n; i++) {
            for(int j = 0; j < squres.size(); j++){
                if(i>=squres.get(j)) {
                    dp[i] = Math.min(dp[i], dp[i - squres.get(j)] + 1);
                }
            }
        }
        return dp[n];
    }
}
