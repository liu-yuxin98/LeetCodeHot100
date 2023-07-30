public class BestTimetoBuyandSellStock_122 {
    public static int maxProfit(int[] prices) {
        int i = 0;
        int j = 0;
        int earn = 0;
        // iterate through prices to find the first pair that p[i] < p[i+1] or reach the end
        while(i<= prices.length-2){
            if(prices[i+1]>prices[i]){
                break;
            }
            i++;
        }
        j = i+1;

        while(j<=prices.length-1){
            if(j==prices.length - 1){
                // reach the end
                earn += prices[j]-prices[i];
                break;
            }
            if (prices[j]<=prices[j+1]){
                // got up till reach local max or end
                j ++;
            } else {
                // local max - prev local min
                earn += prices[j] - prices[i];
                i = j;
                // go down find local min
                while(i<= prices.length-2){
                    if(prices[i+1]<=prices[i]){
                        i ++;
                    } else {
                        break;
                    }
                }
                j = i+1;
            }
        }

        return earn;
    }

}
