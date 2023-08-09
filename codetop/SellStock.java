package codetop;

public class SellStock {
    public int maxProfit(int[] prices) {
        int max =0;
        int [] rightMax = new int[prices.length];
        rightMax[prices.length-1] = prices[prices.length-1];
        for(int i=prices.length-2;i>=0;i--){
            rightMax[i] = Math.max(rightMax[i+1],prices[i]);
        }

        for(int i=0;i<rightMax.length;i++){
            max = Math.max(rightMax[i]-prices[i], max);
        }
        return max;
    }
}
