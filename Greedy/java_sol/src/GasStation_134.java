import java.util.Arrays;

public class GasStation_134 {
    public static int canCompleteCircuit(int[] gas, int[] cost) {
        int [] leftgas = new int[gas.length];
        int [] accumulate_gas = new int[gas.length];
        for(int i = 0; i < gas.length; i++){
            leftgas[i] = gas[i]-cost[i];
        }
        for(int i=0;i<accumulate_gas.length; i++){
            accumulate_gas[i]= leftgas[i];
        }
        for(int i=1;i < accumulate_gas.length; i++){
            accumulate_gas[i] = accumulate_gas[i-1]+accumulate_gas[i];
        }
        if(accumulate_gas[accumulate_gas.length - 1]<0){
            // can not find
            return -1;
        }
//        System.out.println(Arrays.toString(leftgas));
//        System.out.println(Arrays.toString(accumulate_gas));
        // find where is the min gas start from the beginning
        int mingas_index = 0;
        for (int i = 1; i < accumulate_gas.length; i++) {
            if(accumulate_gas[i]<accumulate_gas[mingas_index]){
                mingas_index = i;
            }
        }
        if(accumulate_gas[mingas_index]>=0){
            return 0;
        }
        int mingas = accumulate_gas[mingas_index];
        for(int i=leftgas.length - 1; i >= 0; i--){
            mingas += leftgas[i];
            if(mingas>=0){
                return i;
            }
        }
        return -1;

    }
    public static void main(String[] args) {
        int [] gas = new int[]{5,1,2,3,4};
        int [] cost = new int[] {4,4,1,5,1};
//        int [] gas = new int[]{1,2,3,4,5};
//        int [] cost = new int[] {3,4,5,1,2};
//        int [] gas = new int[]{2,3,4};
//        int [] cost = new int[] {3,4,3};
        int output = canCompleteCircuit(gas,cost);
        System.out.println(output);
    }
}
