package Dynamic_Programming;

import java.util.Arrays;

public class LastStone1049 {
    public int lastStoneWeightII(int[] stones) {
        Arrays.sort(stones);
        int sum = Arrays.stream(stones).sum();
        int half = sum/2;
        int [] dp = new int[half+1];
//        System.out.println(Arrays.toString(stones));
        for(int i=0;i<stones.length;i++){
            for(int j=half;j>=stones[i];j--){
                dp[j] = Math.max(dp[j],dp[j-stones[i]]+stones[i]);
            }
//            System.out.println(Arrays.toString(dp));
        }
        int res = sum-2*dp[half];
//        System.out.println(res);
        return res;
    }
}
