package Dynamic_Programming;

import java.util.Arrays;

public class CoinChange322 {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount+1];
        Arrays.fill(dp,amount+1);
        dp[0] = 0;
        for (int i = 1; i <= amount; i++) {
            for (int j = 0; j <coins.length; j++) {
                if(coins[j]>i){
                    // can not fit
                    continue;
                }
                dp[i] = Math.min(dp[i], dp[i-coins[j]]+1);
            }
        }

        if (dp[amount]== amount+1) {
            return -1;
        }
        return dp[amount];
    }
}
