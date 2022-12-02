import java.util.Arrays;
public class max_sum_of_array_after_k_neg_1005 {
    public static int largestSumAfterKNegations(int[] nums, int k) {
        Arrays.sort(nums);
        // iterate through nums
        for(int i=0;i<nums.length; i++){
            if(k==0){
                break;
            }
            if( nums[i] <0){
                k --;
                nums[i] = -nums[i];
            } else{
                Arrays.sort(nums);
                if(k%2!=0){
                    nums[0] = -nums[0];
                }
                k = 0;
                break;

                }

            }
        if(k>0){
            if(k%2!=0) {
                Arrays.sort(nums);
                nums[0] = -nums[0];
            }
        }

        int sum = 0;
        for(int i=0;i<nums.length;i++){
            sum += nums[i];

        }
        return sum;
    }


    public static void main(String[] args) {
        int [] nums = new int[]{-2,-3,-4};
        int k = 4;
        int value = largestSumAfterKNegations(nums,k);
        System.out.println(value);
    }
}
