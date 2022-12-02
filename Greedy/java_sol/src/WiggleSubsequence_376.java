public class WiggleSubsequence_376 {
    public static int wiggleMaxLength(int[] nums) {
        if(nums.length==1){
            return 1;
        }
        if(nums.length==2){
            if(nums[0]==nums[1]){
                return 1;
            }
            return 2;
        }
        int pre_diff = nums[1]-nums[0];
        int cur_diff = 0;
        int i = 0;
        int cnt = 1;
        // till pre_diff !=0
        while(true){
            if (i>nums.length-2){
                break;
            }
            pre_diff = nums[i+1]-nums[i];
            if(pre_diff!=0){
                cnt += 1;
                break;
            }
            i++;
        }

        while(i<=nums.length-2){
            cur_diff = nums[i+1]-nums[i];
            if(cur_diff*pre_diff<0){
                    cnt ++;
                    pre_diff = cur_diff;
            }
            i ++;
        }
        return cnt;
    }

    public static void main(String[] args) {
        int [] nums = new int[]{0,0,0};
        int output = wiggleMaxLength(nums);
        System.out.println(output);
    }
}
