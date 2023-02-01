package Dynamic_Programming;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class OnesAndZeros474 {
    public int findMaxForm(String[] strs, int m, int n) {
        List<int []> strsData = new ArrayList<int[]>();

        for(String str:strs){
            int zero = 0;
            int one = 0;
            for(int i = 0; i < str.length(); i++){
                if(str.charAt(i) == '0'){
                    zero+=1;
                }else{
                    one += 1;
                }
            }
            strsData.add(new int[]{zero,one});
        }

        int [][] dp = new int[m+1][n+1];
        dp[0][0] = 0;
        for(int i= 0;i<strsData.size(); i++){
            int a = strsData.get(i)[0];
            int b = strsData.get(i)[1];
            for (int j = m; j >= a; j--) {
                for (int k = n; k >= b; k--) {
                    dp[j][k] = Math.max(dp[j-a][k-b]+1,dp[j][k]);
                }

            }
        }

//        strsData.forEach(array->System.out.println(Arrays.toString(array)));
//        System.out.println(Arrays.deepToString(dp));
        return dp[m][n];
    }
}
